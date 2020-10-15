import re, requests

htmlfile = requests.get(input()).text
res = re.findall(r'<a.+?href=(\'|\")(.+?\:\/\/|)(([0-9a-zA-Zа-яА-Я-])+(?:\.([0-9a-zA-Zа-яА-Я-])+){1,2}|)(\.\.\/|\:|\/|).*?(\'|\").*?>', r'<a href="../skip_relative_links"> <a href="http://stepic.org/courses"> <a href=\'https://stepic.org\'> <a href=\'http://neerc.ifmo.ru:1345\'> <a href="ftp://mail.ru/distib" > <a href="ya.ru"> <a href="www.ya.ru"> <a href="../skip_relative_links"> <a href="www.ya.ru/">')

lst = []
for line in res:
    if line[2] !='':
        if line[2] not in lst:
            lst.append(line[2])
lst.sort()
print('\n'.join(lst))
# print(htmlfile)