dna = input()                    # считываем строку
print(dna[0],end='')             # выводим первый символ
cnt = 1                          # счетчик символов на единице
for i in range(0,len(dna)-1):    # итератор проходит по всем индексам символов кроме предпоследнего
    if dna[i] == dna[i+1]:       # сравниваем символ по текущему индексу со следующим
        cnt+=1                   # если символы одинаковые, то увеличиваем счетчик
    else :
        print(cnt,end='')        # если разные, то выводим значение счетчика
        print(dna[i+1],end='')   # выводим следующий символ
        cnt = 1                  # счетчик текущего символа на единице
print(cnt)                       # в конце распечатываем значение счетчика последнего символа

# genome = input()
# i = 0
# s = 1
# g = ''
# for i in range(len(genome) - 1):
#     if genome[i] == genome[i + 1]:
#         s += 1
#     else:
#         g += genome[i]+str(s)
#         s = 1
# print(g+genome[-1]+str(s))

# genome = str(input())
# n = len(genome)
# i = 0
# s = 1
# g = ''
# while i < (n - 1):
#     if genome[i] == genome[i + 1]:
#         s += 1
#     else:
#         g += genome[i]+str(s)
#         s = 1
#     i += 1
# print(g+genome[i]+str(s))