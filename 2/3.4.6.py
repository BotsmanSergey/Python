import requests, re

input1 = input()
input2 = input()
res = requests.get(input1)
finded_links = re.findall(r'<a.*href=\"(.*)\".*>.*</a>', res.text)
cnt = 0
for a in finded_links:
    res_level2 = requests.get(a)
    if res_level2.status_code ==  200:
        if re.search(input2, res_level2.text):
            print("Yes")
            break
    cnt += 1
    if cnt == len(finded_links):
        print("No")

# import requests, re 

# result = False
# link1 = input()
# link2 = input()
# res1 = requests.get(link1)
# for link in re.findall(r'<a.*href=\"(.*)\".*>.*</a>', res1.text):
#     res = requests.get(link)
#     if res.status_code == 200:
#         for url in re.findall(r'<a.*href=\"(.*)\".*>.*</a>', res.text):
#             if link2 == url:
#                 result = True
#                 break
#         if result:
#             break
# if result:
#     print("Yes")
# else:
#     print("No")