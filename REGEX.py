from pprint import pprint
import re
import csv


with open("phonebook_raw.csv", encoding='utf-8') as f:
    rows = csv.reader(f, delimiter="\n")
    contacts_list = list(rows)

pattern = r'(\+7|8)+(\s)?(\()?((\d{3}))(\))?[\-\s]?((\d{3})?)(\-?)(\d{2})?(\-)?(\d{2}?)*\s*\(*(([а-я])*(\.)?)\s*((\d+))?\)*'
replace = r'+7(\5)\8-\10-\12 \13\17'
a = []
for data in contacts_list:
    for i in data:
        res = re.split('[,]+', i)
        if res != ['']:
            a.append(res)

change_contact_list=[]
for item in a:
    new_data = []
    if item[0].count(' ') >=1:
        item_res = re.split('[ ]+', item[0])
        item_res2 = ','.join(item_res)
        new_data.append(item_res2)
        rest_info = ','.join(item[1:])
        new_data.append(rest_info)
    elif item[0].count(',') >= 1:
        new_data.append(item[0])
        rest_info = ','.join(item[1:])
        new_data.append(rest_info)
    elif item[1].count(' ') ==1:
        it_res = re.split('[ ]+', item[1])
        it_res2 = ','.join(it_res)
        full_name = ','.join([item[0], it_res2])
        rest_info = ','.join(item[2:])
        new_data.append(full_name)
        new_data.append(rest_info)
    else:
        info = ','.join(item[0:])
        new_data.append(info)
    change_contact_list.append(new_data)

pprint(change_contact_list)
a_dict = {}

for kl in change_contact_list:
    a_dict_info = {}
    if len(kl) > 1:
        name = kl[0].split(",")
        full_name = ','.join([name[0], name[1]])
        if full_name not in a_dict.keys():
            a_dict[full_name] = a_dict_info
            for n in name:
                if re.findall(r'\w+\вич|вна', n):
                    a_dict_info["surname"] = n
            add_info = kl[1].split(",")
            for ai in add_info:
                if re.findall(r'\w+\вич|вна', ai):
                    a_dict_info["surname"] = ai
                elif re.findall(r'[а-яА-Я]+\s[а-яА-Я]', ai):
                    a_dict_info["position"] = ai
                elif re.findall(r'\w+\@\w+\.\w+',ai):
                    a_dict_info["email"] = ai
                elif re.findall(r'(\+7|8)+(\s)?(\()?((\d{3}))(\))?[\-\s]?((\d{3})?)(\-?)(\d{2})?(\-)?(\d{2}?)*\s*\(*(([а-я])*(\.)?)\s*((\d+))?\)*',ai):
                    result = re.sub(pattern, replace, ai)
                    a_dict_info["phone"] = result
                elif re.findall(r'\w+фин|[А-Я]{3}', ai):
                    a_dict_info["organization"] = ai
        else:
            for n in name:
                if re.findall(r'\w+\вич|вна', n):
                    a_dict_info["surname"] = n
            add_info = kl[1].split(",")
            for ai in add_info:
                if re.findall(r'\w+\вич|вна', ai):
                    a_dict_info["surname"] = ai
                elif re.findall(r'[а-яА-Я]+\s[а-яА-Я]', ai):
                    a_dict_info["position"] = ai
                elif re.findall(r'\w+\@\w+\.\w+',ai):
                    a_dict_info["email"] = ai
                elif re.findall(r'(\+7|8)+(\s)?(\()?((\d{3}))(\))?[\-\s]?((\d{3})?)(\-?)(\d{2})?(\-)?(\d{2}?)*\s*\(*(([а-я])*(\.)?)\s*((\d+))?\)*',ai):
                    result = re.sub(pattern, replace, ai)
                    a_dict_info["phone"] = result
                elif re.findall(r'\w+фин|[А-Я]{3}', ai):
                    a_dict_info["organization"] = ai
            a_dict[full_name].update(a_dict_info)
    if len(kl) == 1:
        name = kl[0].split(",")
        add_info = ','.join(name[2:])
        full_name = ','.join([name[0], name[1]])
        if full_name not in a_dict.keys():
            a_dict[full_name] = a_dict_info
            for ai in name:
                if re.findall(r'\w+\вич|вна', ai):
                    a_dict_info["surname"] = ai
                elif re.findall(r'[а-яА-Я]+\s[а-яА-Я]', ai):
                    a_dict_info["position"] = ai
                elif re.findall(r'\w+\@\w+\.\w+',ai):
                    a_dict_info["email"] = ai
                elif re.findall(r'(\+7|8)+(\s)?(\()?((\d{3}))(\))?[\-\s]?((\d{3})?)(\-?)(\d{2})?(\-)?(\d{2}?)*\s*\(*(([а-я])*(\.)?)\s*((\d+))?\)*',ai):
                    result = re.sub(pattern, replace, ai)
                    a_dict_info["phone"] = result
                elif re.findall(r'\w+фин|[А-Я]{3}', ai):
                    a_dict_info["organization"] = ai
        else:
            for ai in name:
                if re.findall(r'\w+\вич|вна', ai):
                    a_dict_info["surname"] = ai
                elif re.findall(r'[а-яА-Я]+\s[а-яА-Я]', ai):
                    a_dict_info["position"] = ai
                elif re.findall(r'\w+\@\w+\.\w+',ai):
                    a_dict_info["email"] = ai
                elif re.findall(r'(\+7|8)+(\s)?(\()?((\d{3}))(\))?[\-\s]?((\d{3})?)(\-?)(\d{2})?(\-)?(\d{2}?)*\s*\(*(([а-я])*(\.)?)\s*((\d+))?\)*',ai):
                    result = re.sub(pattern, replace, ai)
                    a_dict_info["phone"] = result
                elif re.findall(r'\w+фин|[А-Я]{3}', ai):
                    a_dict_info["organization"] = ai
            a_dict[full_name].update(a_dict_info)
pprint(a_dict)

my_contact_list=[]
for k,v in a_dict.items():
    my_contact_list.append(k)
    for key, value in v.items():
        my_contact_list.append(value)


with open("phonebook.csv", "w", encoding='utf-8') as f:
    datawriter = csv.writer(f, delimiter=" ")
    datawriter.writerows(my_contact_list)
