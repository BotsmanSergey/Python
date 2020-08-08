class MyDictionary(dict):
    def add_key(self, lst):
        if self.get(lst[0]) == None:
            if len(lst) > 1:
                self[lst[0]]=[]
                for i in lst[2:]:
                    self[lst[0]].append(i)
        else:
            if len(lst) > 1:
                for i in lst[2:]:
                    self[lst[0]].append(i) 
def found_parents(a, b):
    if d.get(a) != None:
        for i in d[a]:
            for j in d2:
                if i == j:
                    print(b)
                    return True
            else: 
                if found_parents(i, b):
                    return True
n = int(input())
d = MyDictionary()
for i in range(n):
    a = list()
    a = input().strip().split()
    d.add_key(a) #create class and method for learning
n2 = int(input())
d2 = []
d2.append(input()) # first pass becouse nothink сравнивать
for i in range(1, n2):
    can = False
    g = input()
    d2.append(g)
    # for k in range(0, i -1):
    #     if d2[k] == g:
    #         print(g)
    #         can = True
    #         break
    # if can == False:    
    #     found_parents(d2[i], d2[i])
    found_parents(d2[i], d2[i])