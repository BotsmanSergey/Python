import requests
r ='https://stepic.org/media/attachments/course67/3.6.3/699991.txt'
b =[0]
while b[0] != 'We':
	r = requests.get(r)
	b = r.text.strip().split()
	print(r.text)
	r = str('https://stepic.org/media/attachments/course67/3.6.3/') + r.text.strip()