import csv, re

d = {}

def d_add(vol):
    if vol not in d:
        d[vol] = 1
    else: d[vol] += 1

with open("Crimes.csv") as f:
    reader = csv.reader(f)
    for row in reader:
        if re.search(r'2015', row[2]):
            d_add(row[5])
maxx = 0
maxxc = ''
for i in d:
    if d[i] > maxx:
        maxx = d[i]
        maxxc = i
print(maxxc, maxx)

