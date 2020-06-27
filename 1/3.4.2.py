s = ''
alpha = ''
digit = ''
with open ('readfile.txt', 'r') as inf:
    for i in inf:
        i = i.strip()
        for j in range(len(i)):
            if i[j].isdigit():
                if i[j-1].isdigit():
                    digit += i[j]
                else: digit = i[j]
                if j+1 == len(i):
                    s += alpha * int(digit)
                elif i[j+1].isalpha():
                    s += alpha * int(digit)
            else: alpha = i[j]
                
            #s += alpha * int(digit)
with open ('writefile.txt', 'w') as out:
    out.write(s)
