import re, requests

htmlfile = requests.get(input()).text
res = re.findall(r'<a.+?href.*?=.*?(\'|\")(.+?\:\/\/|)(([0-9a-zA-Zа-яА-Я.-])+|)(\.\.\/|\:|\/|).*?(\'|\").*?>', htmlfile, flags=re.MULTILINE)
lst = []
for line in res:
    if line[2] !='':
        if line[2] not in lst:
            lst.append(line[2])
lst.sort()
print('\n'.join(lst))

# import requests, re
# urls = set(re.findall(r"(?:.*)?(?:<a(?:.*)? href=[\"\'])(?:\w+://)?(\w[\w\.-]*)", requests.get(input()).text))

# print('\n'.join(sorted(urls)))