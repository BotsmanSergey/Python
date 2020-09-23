import sys, re
[print(line.rstrip()) for line in sys.stdin if re.search(r'(\b\w+)\1\b', line)]