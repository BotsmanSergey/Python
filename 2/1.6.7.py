def func(parent, chield):
    if parent in d[chield]:
        return True
    elif len(d[chield]) == 0:
        return None
    else:
        cnt = 0
        for i in d[chield]:
            x = func(parent, i)
            if x == None:
                cnt += 1
            elif x == True:
                return True
            if cnt == len(d[chield]):
                return False
n = int(input())
d = {}
for i in range(n):
    lst = list()
    lst = input().strip().split()
    if len(lst) == 1:
        if d.get(lst[0]) == None: d[lst[0]] = [] 
    else:
        if d.get(lst[0]) == None:
            d[lst[0]] = []
            for i in lst[2:]:
                if i not in d[lst[0]]:
                    d[lst[0]].append(i)
        else:
            for i in lst[2:]:
                if i not in d[lst[0]]:
                    d[lst[0]].append(i)
#print(d)
n2 = int(input())                    
lst3 = []
for i in range(n2):
    lst3 = input().strip().split()
    #print(lst3)
    if d.get(lst3[1]) == None:
        print('No')
    elif lst3[0] == lst3[1]:
        print('Yes')
    else:
        v = func(lst3[0], lst3[1])
        if v == True:
            print('Yes')
        else: print('No')