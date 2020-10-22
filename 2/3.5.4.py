import json

def d_add(class_info):
    if d.get(class_info["name"]) == None:
        d[class_info["name"]] = class_info['parents']

def ch_search(i):
    if d[i] != []:
        for j in d[i]:
            if i not in ch[j]:
                ch[j].append(i)

def descendant_search(i):
    if d[i] != []:
        for j in d[i]:
            if i not in descendant[j]:
                descendant[j].append(i)
            if ch[i] != []:
                for k in descendant[i]:
                    if k not in descendant[j]:
                        descendant[j].append(k)    
            descendant_search(j)
    else:
        if ch[i] != []:
                for k in ch[i]:
                    if k not in descendant[i]:
                        descendant[i].append(k)

d = {} # dict of parents
ch ={} # dict of chields
descendant = {} # словарь потомков

data_py = json.loads(input())
for class_info in data_py:
    d_add(class_info) 
for i in d:
    ch[i] = []
    descendant[i] = []
for i in ch:
    ch_search(i)
for i in descendant:
    descendant_search(i)

for key in sorted(descendant):
    print(key, ":", len(descendant[key])+1)

print(d)
print(ch)
print(descendant)