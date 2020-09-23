import sys, re

for line in sys.stdin:
    line = line.rstrip()
    line = re.sub(r'human', 'computer', line)
    print(line)
    # print(re.sub(r'human', 'computer', sys.stdin.read()), end='')