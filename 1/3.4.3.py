
def maxd(dictionary):
    v = 0
    k = ''
    for i in dictionary:
        if dictionary[i]> v:
            v = dictionary[i]
            k = i
        elif dictionary[i] == v:
            if k < i:
                k = i
    return k, v
d = {}
with open ('readfile1.txt', 'r') as inf:
    l = inf.read().strip().lower().split()
    for i in l:
        if i in d:
            d[i] += 1
        else: d[i] = 1
    key, value = maxd(d)
with open ('writefile1.txt', 'w') as out:
    out.write(str(key) + ' ' + str(value))