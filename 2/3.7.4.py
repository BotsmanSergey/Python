from xml.etree import ElementTree

def get_Children(root, level):
    d[root.attrib["color"]] += level
    if len(root) != 0:
        level += 1
        for child in root:
            get_Children(child, level)

d = {"red":0, "green":0, "blue":0}

root = ElementTree.fromstring(input())
get_Children(root, 1)
print(d['red'], d['green'], d['blue'])