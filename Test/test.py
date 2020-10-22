import json

d = {}

data_py = json.loads(input())
for class_info in data_py:
    print(class_info["name"]) 
print(d)