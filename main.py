
from pprint import pprint
import requests

#Задача 1 ___________________________________________________________

def intelligence_hero(name):
    url = "https://superheroapi.com/api/2619421814940190/search/"
    response = requests.get(url + name, timeout=3)
    json = response.json()
    intelligence = json['results'][0]['powerstats']['intelligence']
    return int(intelligence)

def max_intelligence(name1, i1, name2, i2, name3, i3):
    max = 0
    if i1 > max:
        i1 = max
        name = name1
    if i2 > max:
        i2 = max
        name = name2
    if i3 > max:
        i3 = max
        name = name3
    print(f'Самый умный супергерой: {name}')


if __name__ == '__main__':

    i1 = intelligence_hero("Hulk")
    i2 = intelligence_hero("Captain America")
    i3 = intelligence_hero("Thanos")

    max_intelligence("Hulk", i1, "Captain America", i2, "Thanos", i3)
#
#
# #
# #Задача 2  ____________________________________________________
# #
#
class YaUploader:

    def __init__(self, token):
        self.token = token

    def get_headers(self):
        return {
            'Content-Type': 'application/json',
            'Authorization': 'OAuth {}'.format(self.token)
        }

    def _get_upload_link(self, file_path):
        upload_url = "https://cloud-api.yandex.net/v1/disk/resources/upload"
        headers = self.get_headers()
        params = {"path": file_path, "overwrite": "true"}
        response = requests.get(upload_url, headers=headers, params=params)
        pprint(response.json())
        return response.json()

    def upload(self, file_path, file_name ):
        href = self._get_upload_link(file_path=file_path).get("href", "")
        response = requests.put(href, data=open(file_name, 'rb'))
        response.raise_for_status()
        if response.status_code == 201:
            print("Success")


if __name__ == '__main__':

    path_to_file = "netology/test_my_home_work.txt"
    token = ""
    file_name = "test_home_work.txt"

    uploader = YaUploader(token)
    uploader.upload(path_to_file, file_name)