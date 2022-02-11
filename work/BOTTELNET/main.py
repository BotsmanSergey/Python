import telnetlib
import time

host = 'telehack.com'
password = 'clock'
command = 'pwd'


telnet = telnetlib.Telnet(host)
#print(telnet.read_until(b'key'))
print(1)
time.sleep(2)
all_result = telnet.read_very_eager().decode('utf-8')
print(all_result)
print(2)
telnet.write(b'\n')

print(3)
telnet.write(password.encode('ascii') + b'\n')
telnet.write(command.encode('ascii') + b'\n')
post = telnet.read_until(b'key')
print(post)
time.sleep(2)
print(4)
print(telnet.read_until(b'key'))
print(5)

telnet.write(b'y')
post = telnet.read_until(b'key')
print(post)
time.sleep(2)

post = telnet.read_until(b'key')
print(post)

telnet.write(b'y')
time.sleep(2)

post = telnet.read_until(b'key')
print(post)

telnet.close()
