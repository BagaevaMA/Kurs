token_vk = input('Введите ключ пользователя VK')
token_yandex = input('Введите токен Яндекс Диска')
token_vk
user_id = input('Введите id пользователя ВКонтакте')

import requests
from pprint import pprint
from datetime import datetime
import os
import json
import sys
import time
from tqdm import tqdm


class VkUser:
    url = 'https://api.vk.com/method/'

    def __init__(self, token_vk, version):
        self.params = {
            'access_token': token_vk,
            'v': version
        }

    def get_photos(self, user_id):
        get_photos_url = self.url + 'photos.get'
        album = input('Введите album_id: wall — фотографии со стены,profile — фотографии профиля или id альбома')
        get_photos_params = {
            'user_id': user_id,
            'album_id': album,
            'rev': 1,
            'extended': 1
        }
        getphotos = requests.get(get_photos_url, {**self.params, **get_photos_params}).json()
        return getphotos['response']['items']


class YandexDisk:
    host = 'https://cloud-api.yandex.net:443/'

    def __init__(self, token_yandex):
        self.token = token_yandex

    def get_headers(self):
        return {'Content-Type': 'application/json', 'Authorization': f'OAuth {self.token}'}

    def create_folder(self):
        uri = 'v1/disk/resources/'
        url = self.host + uri
        new_folder_name = input('Введите название новой папки, в которую будут сохранены фото')
        path = f'/{new_folder_name}'
        params = {'path': path}
        response = requests.put(url, headers=self.get_headers(), params=params)
        if response.status_code == "201":
            print('Папка {new_folder_name} успешно создана')
        return (new_folder_name)

    def upload_photo(self, list_photo):
        new_folder = self.create_folder()
        number_of_photo = int(input('Введите количество фото, которые надо сохранить'))
        data = {}
        data['files_photo'] = []
        for photo in list_photo[0:number_of_photo]:
            uri = 'v1/disk/resources/upload/'
            url = self.host+uri
            disk_file_name = str(photo['likes'])
            photo_url = photo['url']
            path_to = f'/{new_folder}/{disk_file_name}.jpg'
            params = {'path': path_to, 'url': photo_url}
            response = requests.post(url, headers=self.get_headers(), params = params)
            answer = str(response.status_code)
            resolution = '.jpg'
            file_name = disk_file_name+resolution
            data['files_photo'].append({"file_name": file_name,
                                        "size": photo['height']})
            if answer.startswith('2'):
                print('Загрузка прошла успешно')
        return(data)



    def create_file(self, file_for_write):
        with open('data.txt', 'w') as outfile:
            json.dump(file_for_write, outfile)
        return


if __name__ == "__main__":

    ya = YandexDisk(token_yandex)
    vk_client = VkUser(token_vk, '5.131')
    getphotos = vk_client.get_photos(user_id)

    photo_list = []

    for picture in tqdm(getphotos):
        photo = {}
        for key, value in picture.items():
            if key == 'id':
                photo[key] = value
            elif key == 'date':
                ts = int(value)
                dt = datetime.utcfromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
                photo[key] = dt
            elif key == 'likes':
                for count, number in value.items():
                    if count == 'count':
                        photo[key] = number
            elif key == 'sizes':
                for size in value:
                    for parametrs, amount in size.items():
                        sort_size = sorted(value, key=lambda d: d['height'])
                        photo['height'] = sort_size[-1]['height']
                        photo['url'] = sort_size[-1]['url']
            time.sleep(0.001)
        photo_list.append(photo)

    ya.create_file(ya.upload_photo(photo_list))