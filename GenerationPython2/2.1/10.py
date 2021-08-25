'''n человек, пронумерованных числами от 11 до nn, стоят в кругу. Они начинают считаться, каждый kk-й по счету человек выбывает из круга, после чего счет продолжается со следующего за ним человека. Напишите программу, определяющую номер человека, который останется в кругу последним.

Формат входных данных
На вход программе подаются два числа nn и kk, записанные на отдельных строках.

Формат выходных данных
Программа должна вывести одно число – номер человека, который останется в кругу последним.

Примечание 1. Подробнее ознакомиться с классической задачей Иосифа Флавия можно тут.

Примечание 2. Визуализацию работы алгоритма можно посмотреть тут.

Тестовые данные 🟢
Sample Input 1:

2
1
Sample Output 1:

2
Sample Input 2:

5
2
Sample Output 2:

3
Sample Input 3:

7
5
Sample Output 3:

6'''
index = 0
def addIndex():
    global index
    if len(players) == index + 1:
                index = 0
    else:
        index+=1

a = int(input())
b = int(input())
players = [i + 1 for i in range(a)]
print(players)

for i in range(a-1):
    for j in range(b-1):
        addIndex()
        print(str(index)+' index')
        while (players[index] == 'X'):
            addIndex()
        print(str(index)+' index while')
    players[index] = 'X'
    print(players)
    addIndex()
    print(str(index)+' index2')
    while(players[index] == 'X'):
        addIndex()
    print(str(index)+' index while2')
print(players[index])

    

