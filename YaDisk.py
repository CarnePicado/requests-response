from pprint import pprint

import requests


class YaDisk:
    #host = 'https://cloud-api.yandex.net'

    def __init__(self, token):
        self.token = token

    def get_headers(self):
        return {
            'Content-Type': 'application/json', 
            'Authorization': f'OAuth {self.token}'
        }

    def get_files_list(self):
        url = 'https://cloud-api.yandex.net/v1/disk/resources/files'
        headers = self.get_headers
        response = requests.get(url, headers=headers)
        return response.json()

    def _get_upload_link(self, path):
        url = 'https://cloud-api.yandex.net/v1/disk/resources/'
        headers = self.get_headers()
        params = {'path': path, 'overwrite': True}
        response = requests.get(url, params=params, headers=headers)
        return response.json()

    def upload_file(self, path, file_name):
        href = self._get_upload_link(path=path).get('href','')
        response = requests.put(href, data=open(file_name, 'rb'))
        response.raise_for_status()
        if response.status_code == 201:
            print('Success')