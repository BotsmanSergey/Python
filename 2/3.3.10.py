import sys, re
pattern = r"\\" 

for line in sys.stdin:
    line = line.rstrip()
    match = re.findall(pattern, line)
    if len(match)> 0:
        print(line)
# [print(line.rstrip()) for line in sys.stdin if re.search(r'\\', line)]