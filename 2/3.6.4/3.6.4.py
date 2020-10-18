# имя	Botsman.pro
# ID клиента	c8415c744bc851e61138
# Секрет клиента	d82f39bad7cace40c018a6a087ae8b7e

import requests
import json

client_id = 'c8415c744bc851e61138'
client_secret = 'd82f39bad7cace40c018a6a087ae8b7e'

# инициируем запрос на получение токена
r = requests.post("https://api.artsy.net/api/tokens/xapp_token",
                  data={
                      "client_id": client_id,
                      "client_secret": client_secret
                  })

# разбираем ответ сервера
j = json.loads(r.text)

# достаем токен
token = j["token"]



# создаем заголовок, содержащий наш токен
headers = {"X-Xapp-Token" : token}
# инициируем запрос с заголовком
d = {}
with open("readfile.txt", 'r') as f:
    for line in f:
        r = requests.get("https://api.artsy.net/api/artists/" + line.strip(), headers=headers)
        r.encoding = 'utf-8'
        # разбираем ответ сервера
        j = json.loads(r.text)
        if d.get(j['birthday']) == None:
            d[j['birthday']] = [j['sortable_name']]
        else:
            d[j['birthday']].append(j['sortable_name'])
            d[j['birthday']].sort()
for key in sorted(d):
    for i in d[key]:
        print(i)



