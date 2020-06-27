import requests
with open ('readfile3.txt', 'r') as inf:
	a = inf.read().strip()
r = requests.get(a)
n = len(r.text.splitlines())
print(n)