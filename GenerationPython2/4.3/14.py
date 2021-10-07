a = [i for i in input().split()]
b = [[]]
for i in range(len(a)):
    for j in range(len(a)-i):
        b.append(a[j:j+i+1])
print(b)