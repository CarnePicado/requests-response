import requests

int_heroes_list = ['Hulk', 'Captain America', 'Thanos']
int_heroes_dict = {}
url = 'https://akabab.github.io/superhero-api/api'
resp = requests.get(url + '/all.json')
j_resp = resp.json()
for i in j_resp:
    if i['name'] in int_heroes_list:
        int_heroes_dict[i['name']] = int(i['powerstats']['intelligence'])

print(f'''Самый умный супер герой- {max(int_heroes_dict, key=int_heroes_dict.get)}''')