import sys
import re
pattern = r"cat"

for line in sys.stdin:
    line = line.rstrip()
    # process line
    match = re.findall(pattern, line)
    if len(match)> 1:
        print(line)
    else: continue
