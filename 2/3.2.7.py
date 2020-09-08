s = input()
t = input()
count = 0
for i in range(len(s)-len(t)+1):
    if s[i:].startswith(t):
        count += 1
print(count)
# print(sum(1 for i in range(len(s)) if s.startswith(t, i)))