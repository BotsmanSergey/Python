with open ('readfile2.txt', 'r') as inf:
	l = inf.read().split('\n')
	for i in range(len(l)):
		l[i] = l[i].split(';')
with open ('writefile2.txt', 'w') as out:
	for i in l:
		a = 0
		for j in range(1, len(i)):
			a += int(i[j])
		out.write(str(int(a)/(len(i)-1))+'\n')
	for i in range(1, len(l[0])):
		s = 0
		for j in range(len(l)):
			#print (l[j][i])
			s += int(l[j][i])
		out.write(str(s/len(l))+' ')