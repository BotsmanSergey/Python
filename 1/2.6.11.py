a = int(input())
b = [[0 for j in range(a)] for i in range(a)]
s = 0
n = 1
for i in range(a):
    if s == a ** 2:
        break
    else:
        for j in range(a - n + 1):
            if b[i][j] == 0:
                s += 1
                b[i][j] = s
        for i in range(a - n + 1):
            if b[i][j] == 0:
                s += 1
                b[i][j] = s
        for j in range(a - n, n - 2, -1):
            if b[i][j] == 0:
                s += 1
                b[i][j] = s
        for i in range(a - n, n - 1, -1):
            if b[i][j] == 0:
                s += 1
                b[i][j] = s
        n += 1
for i in range(a):
    for j in range(a):
        print(b[i][j], end=' ')
    print()