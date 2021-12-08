import re, os

current_dir = os.path.dirname(os.path.abspath(__file__))

with open(os.path.join(current_dir,'trash.txt'), 'r') as trash:
    trash = trash.read()
    pattern = r"(10\.(3|107)\.\d{1,4}\.\d{1,4})"    
    all_inclusions = re.findall(pattern, trash) # выводит все подходящие шаблоны
    all_inclusions = [i[0] for i in all_inclusions]
    all_inclusions = set(all_inclusions)

with open(os.path.join(current_dir,'list_ip.txt'), 'a') as list_ip:
    for i in sorted(all_inclusions):
        list_ip.write(str(i)+ '\n')
