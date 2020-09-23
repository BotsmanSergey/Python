import sys, re
pattern = r"z\w{3}z" # r'z...z' # r"z.{3}z"

for line in sys.stdin:
    line = line.rstrip()
    match = re.findall(pattern, line)
    if len(match)> 0:
        print(line)
# [print(line.rstrip()) for line in sys.stdin if re.search(r'z...z', line)]