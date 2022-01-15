
import os

current_dir = os.path.dirname(os.path.abspath(__file__))

# with open(os.path.join(current_dir,'commands.txt'),'rb') as commands_file:
#             commands = []
#             for line in commands_file:
#                 line = line.strip().decode(encoding='UTF-8')
#                 if line == '':
#                     continue
#                 commands.append(line)
# print(commands)

s = open(os.path.join(current_dir,'UTF8withBOM.txt'), mode='r', encoding='utf-8-sig').read()
open(os.path.join(current_dir,'UTF8withBOM.txt'), mode='w', encoding='utf-8').write(s)
    
        