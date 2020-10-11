import re, sys

for line in sys.stdin:
    line = line.rstrip()
    line = re.sub(r"\b(\w)(\w)", r'\2\1', line)
    print(line)
    # m = re.match(r"\b(\w)(\w)", "this is") 
    # print(m.groups()) # show groups


