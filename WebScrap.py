import requests
from fake_headers import Headers
from pprint import pprint
from bs4 import BeautifulSoup
import unicodedata
import json

HOST = 'https://spb.hh.ru/search/vacancy?text=python&area=1&area=2'



def get_headers():
    return Headers(browser = 'firefox', os = 'win').generate()

def get_text(url):
    return requests.get(url, headers=get_headers()).text

final_links_list = []
salary_list = []
location_list = []
company_name_list = []
total_data_list = []

def get_links():
    html = get_text(HOST)
    bs = BeautifulSoup(html, 'lxml')
    vacancy_list = bs.find_all('a', class_='serp-item__title')
    links_list = []
    presence_list = []
    for vacancy in vacancy_list:
        links = vacancy['href']
        links_list.append(links)
        html_links = get_text(links)
        links_parsed = BeautifulSoup(html_links, 'lxml')
        descriptions = links_parsed.find('div', {'data-qa': 'vacancy-description'})
        if not descriptions:
            continue
        if ('Django' or 'django' or 'Flask' or 'flask') in descriptions.text:
            presence_list.append('+')
        else:
            presence_list.append('-')
    for i, c in zip(links_list, presence_list):
        if c == "+":
            final_links_list.append(i)
    return final_links_list

get_links()


def get_salary():
    for link in final_links_list:
        salary_link = requests.get(link, headers=get_headers())
        salary_parsed = BeautifulSoup(salary_link.text, 'lxml')
        salary = salary_parsed.find('span', class_="bloko-header-section-2 bloko-header-section-2_lite")
        if not salary:
            salary_list.append('Заработная плата не указана')
        salary_text = salary.text
        salary_normalized = unicodedata.normalize('NFKD', salary_text)
        salary_list.append(salary_normalized)
    return salary_list

get_salary()

def get_comp_name():
    for link in final_links_list:
        comp_name_link = requests.get(link, headers=get_headers())
        comp_name_parsed = BeautifulSoup(comp_name_link.text, 'lxml')
        comp_name = comp_name_parsed.find('a', class_="bloko-link bloko-link_kind-tertiary")
        if not comp_name:
            continue
        comp_name = comp_name['href']
        company_name_href = f'https://spb.hh.ru{comp_name}'
        company_name_link_2 = requests.get(company_name_href, headers=get_headers())
        company_name_parsed_2 = BeautifulSoup(company_name_link_2.text, 'lxml')
        company_name_2 = company_name_parsed_2.find('span', class_="company-header-title-name")
        if not company_name_2:
            continue
        company_name_2_text = company_name_2.text
        company_name_normalized = unicodedata.normalize('NFKD', company_name_2_text)
        company_name_list.append(company_name_normalized)
    return company_name_list
get_comp_name()


def get_location():
    for link in final_links_list:
        location_link = requests.get(link, headers=get_headers())
        location_parsed = BeautifulSoup(location_link.text, 'lxml')
        location = location_parsed.find('p', {'data-qa': 'vacancy-view-location'})
        if not location:
            location = location_parsed.find('span', {'data-qa': 'vacancy-view-raw-address'})
            if not location:
                continue
        location_text = location.text
        location_list.append(location_text)
    return location_list


get_location()
def total_data(any_links, any_salaries, any_companies_names, any_locations):
    all_data = zip(any_links, any_salaries, any_companies_names, any_locations)
    for link, salary, company_name, location in all_data:
        data_dict = {'link': link,
                     'salary': salary,
                     'company_name': company_name,
                     'location': location}
        total_data_list.append(data_dict)
    return total_data_list


total_data(final_links_list, salary_list, company_name_list, location_list)


with open('total_data.json', 'w', encoding='utf-8') as data:
    json.dump(total_data_list, data, indent=2, ensure_ascii=False)