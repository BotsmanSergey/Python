import paramiko, time, os, getpass

print('---НАЧАЛО РАБОТЫ---')
user = input('ВВЕДИТЕ ЛОГИН: ')
secret = getpass.getpass('ВВЕДИТЕ ПАРОЛЬ: ')
port = 22
short_pause = 1

current_dir = os.path.dirname(os.path.abspath(__file__))

#чтение файла ip
with open(os.path.join(current_dir,'list_ip.txt'), 'r') as list_ip_file:
    list_ip = []
    for line in list_ip_file:
        line = line.strip()
        if line == '':
            continue
        list_ip.append(line)

#чтение файла команд
with open(os.path.join(current_dir,'comands.txt'),'r') as comands_file:
            comands = []
            for line in comands_file:
                line = line.strip()
                if line == '':
                    continue
                comands.append(line)

for ip in list_ip: 
    host = ip
    print('---', ip, '---')

    try:
        client = paramiko.SFTPClient
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        # Подключение
        client.connect(hostname=host, username=user, password=secret, port=port)
        client.chdir
        
        # Выполнение команды
        for comand in comands:
            stdin, stdout, stderr = client.exec_command(comand)
            print('---comand:', comand, '---')
            
            time.sleep(short_pause)

            # Читаем результат
            data = stdout.read().decode(encoding='UTF-8') +  stderr.read().decode(encoding='UTF-8')
            print(data)
            
        client.close()
        
        with open(os.path.join(current_dir,'list_ip_good.txt'), 'a') as list_ip_good_file:
            list_ip_good_file.write(str(ip)+'\n')


    except TimeoutError:
        print('не получен нужный отклик, или было разорвано уже установленное соединение')
        with open(os.path.join(current_dir,'list_ip_bad.txt'), 'a') as list_ip_good_bad:
            list_ip_good_bad.write(str(ip)+ '\n')

print('\n\n  ---КОНЕЦ ВСЕХ ОПЕРАЦИЙ---')
