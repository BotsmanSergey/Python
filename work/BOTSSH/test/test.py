
import os

current_dir = os.path.dirname(os.path.abspath(__file__))

with open(os.path.join(current_dir,'commands.txt'),'rb') as commands_file:
            commands = []
            for line in commands_file:
                line = line.strip().decode(encoding='UTF-8')
                if line == '':
                    continue
                commands.append(line)
print(commands)
            