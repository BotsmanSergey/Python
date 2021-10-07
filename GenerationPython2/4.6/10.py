n, m = (int(i) for i in input().split())
a = [['*'] * m for _ in range(n)]
count = 1
circle = 0
i = 0
while(count <= m * n):
    if count > m * n:
            break
    for j in range(0+circle, m-circle):
        a[i][j]=count
        count +=1
        if count > m * n:
            break
    if count > m * n:
            break
    for i in range(1+circle, n-circle):
        a[i][j]=count
        count +=1
        if count > m * n:
            break
    if count > m * n:
            break
    for j in range(m-2-circle, -1+circle, -1):
        a[i][j]=count
        count +=1
        if count > m * n:
            break
    if count > m * n:
            break
    for i in range(n-2-circle, 0+circle, -1):
        a[i][j]=count
        count +=1
        if count > m * n:
            break    
    circle += 1
for i in a:print(*i)