import datetime
# (y, m, d) = [int(i) for i in input().split()]
# date = datetime.date(y, m, d)
date = datetime.date(*[int(i) for i in input().split()]) #объединение двух верхних строк в одну
days = datetime.timedelta(days = int(input()))
# print((date + days).strftime("%Y %-m %-d")) # строка для Unix
print((date + days).strftime("%Y %#m %#d")) # строка для Windows
