a = float(input())
b = float(input())
c = a/(b**2)
if (c>=18.5 and c<=25):
    print('Оптимальная масса')
elif (c>25):
    print('Избыточная масса')
else: 
    print('Недостаточная масса')