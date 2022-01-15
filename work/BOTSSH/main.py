import threading, paramiko, time, getpass, os

strdata=''
fulldata=''
alldata=''
current_dir = os.path.dirname(os.path.abspath(__file__))

class ssh:
    shell = None
    client = None
    transport = None

    def __init__(self, address, username, password):
        print("Connecting to server on ip", str(address) + ".")
        self.client = paramiko.client.SSHClient()
        self.client.set_missing_host_key_policy(paramiko.client.AutoAddPolicy())
        self.client.connect(address, username=username, password=password, look_for_keys=False)
        self.transport = paramiko.Transport((address, 22))
        self.transport.connect(username=username, password=password)

        thread = threading.Thread(target=self.process)
        thread.daemon = True
        thread.start()

    def close_connection(self):
        if(self.client != None):
            self.client.close()
            self.transport.close()

    def open_shell(self):
        self.shell = self.client.invoke_shell()

    def send_shell(self, command):
        if(self.shell):
            self.shell.send(command + "\n")
        else:
            print("Shell not opened.")

    def process(self):
        global strdata, fulldata, alldata
        while True:
            # Print data when available
            if self.shell is not None and self.shell.recv_ready():
                alldata = self.shell.recv(1024)
                while self.shell.recv_ready():
                    alldata += self.shell.recv(1024)                
                strdata = strdata + str(alldata.decode(encoding='UTF-8'))
                
                fulldata = fulldata + str(alldata)
                strdata = self.print_lines(strdata) # print all received data except last line
                

    def print_lines(self, data):
        last_line = data
        if '\n' in data:
            lines = data.splitlines()
            for i in range(0, len(lines)-1):
                print(lines[i])
            last_line = lines[len(lines) - 1]
            if data.endswith('\n'):
                print(last_line)
                last_line = ''
        return last_line

#преобразование кодировки UTF-8 with BOM to UTF-8        
s = open(os.path.join(current_dir,'list_ip.txt'), mode='r', encoding='utf-8-sig').read()
open(os.path.join(current_dir,'list_ip.txt'), mode='w', encoding='utf-8').write(s)

s = open(os.path.join(current_dir,'commands.txt'), mode='r', encoding='utf-8-sig').read()
open(os.path.join(current_dir,'commands.txt'), mode='w', encoding='utf-8').write(s)

#чтение файла ip
with open(os.path.join(current_dir,'list_ip.txt'), 'rb') as list_ip_file:
    list_ip = []
    for line in list_ip_file:
        line = line.strip().decode(encoding='UTF-8')
        if line == '':
            continue
        list_ip.append(line)

#чтение файла команд
with open(os.path.join(current_dir,'commands.txt'),'rb') as commands_file:
            commands = []
            for line in commands_file:
                line = line.strip().decode(encoding='UTF-8')
                if line == '':
                    continue
                commands.append(line)



print('--- НАЧАЛО РАБОТЫ ---')
sshServer = "10.3.136.141"
sshUsername = input('ВВЕДИТЕ ЛОГИН: ')
sshPassword = getpass.getpass('ВВЕДИТЕ ПАРОЛЬ: ')
short_pause = int(input('ВВЕДИТЕ ВРЕМЯ ОЖИДАНИЯ МЕЖДУ КОММАНДАМИ В СЕКУНДАХ: '))



for sshServer in list_ip: 
    print('---', sshServer, '---')
    try:
        connection = ssh(sshServer, sshUsername, sshPassword)
        connection.open_shell()
        for command in commands:
            print('---', command)
            connection.send_shell(command)      
            time.sleep(short_pause)
                  
        connection.close_connection()
        
        with open(os.path.join(current_dir,'list_ip_good.txt'), 'a') as list_ip_good_file:
            list_ip_good_file.write(str(sshServer)+'\n')


    except TimeoutError:
        print('не получен нужный отклик, или было разорвано уже установленное соединение')
        with open(os.path.join(current_dir,'list_ip_bad.txt'), 'a') as list_ip_good_bad:
            list_ip_good_bad.write(str(sshServer)+ '\n')
    except paramiko.AuthenticationException:
        print('Authentication failed')
        with open(os.path.join(current_dir,'list_ip_bad.txt'), 'a') as list_ip_good_bad:
            list_ip_good_bad.write(str(sshServer)+ '\n')
    finally: 
        try:
            connection.close_connection()
            
        except NameError:
            pass
        finally: print('---', sshServer, 'close---')

            
print('\n  --- КОНЕЦ ВСЕХ ОПЕРАЦИЙ ---\n')