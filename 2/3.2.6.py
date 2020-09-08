s = input()
a = input()
b = input()
if (a == b) and (a in s):
    print("Impossible")
else:
    count = 0
    while a in s:
        count += 1
        s = s.replace(a, b)
        if count >= 1000:
            break
    if count >= 1000:
        print("Impossible")
    else: print(count)