import sys, re
[print(line.rstrip()) for line in sys.stdin if re.search(r'(\b\d\b', line)]