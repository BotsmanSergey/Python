import re, requests

with open('readfile.txt', 'r') as inf:
    for line in inf:
        line = line.strip()
        res = re.sub(r'<a.+href=(\"|\')(http:|https:|ftp:|.*)(\w.\w.w|\w.\w)(\/|\:).*>', r'\3', line)
        
