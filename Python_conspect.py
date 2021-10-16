from typing import AsyncIterable, Counter


Ctrl + / #Быстро добавить комментарий
Ctrl + G #Перейти к строке под номером
Alt + ↑ / ↓ #Поменять строку местами с соседними
Shift + Alt + ↓ / ↑ #Дублировать строку
Ctrl + Shift + \ #Перейти к парной скобке
Shift + Alt + F #Отформатировать документ (pep8)
F12 #Перейти к объявлению переменной
Alt + Z #Включить/выключить перенос слов
Ctrl + K Z #Включить дзен-режим
https://nikomedvedev.ru/other/vscodeshortcuts/hotkeys.html


cd #выбор дирректории
python # запуск интерпритатора 
quit #выход из интерпритатора
python test.py # запуск файла

print("Hello", name)
int(-2.3) --> -2
floal(5) --> 5
type(7) --> int # вычесление типа
s = int(input('Введите данные')) # ждет данные от пользователя и переводит в int и сохраняет в s
type(s) -->int

x y or and not
0 0 0  0   1
0 1 1  0   1
1 0 1  0   0
1 1 1  1   0
# по порядку вычисления not and or

10 > 2 and 10 > 9         # True
10 > 2 and 10 > 11        # False
10 > 2 or 10 > 11         # True
10 > 2 and not 10 > 11    # True
not (10 > 2 or 10 > 11)   # False

#True = 1, False = 0
print(True + True + True - False)-->3
print(True + (False / True))-->1.0

#сокращения
if flag: #if flag == True:
if not flag: #if flag == False:

#Для приведения других типов данных к булеву существует функция bool(), работающая по следующим 
# соглашениям:
#строки: пустая строка — ложь (False), непустая строка — истина (True);
#числа: нулевое число — ложь (False), ненулевое число (в том числе и меньшее нуля) — истина (True);
#списки: пустой список — ложь (False), непустой — истина (True).
print(bool('Beegeek'))-->True
print(bool(17))-->True
print(bool(['apple', 'cherry']))-->True
print(bool())-->False
print(bool(''))-->False
print(bool(0))-->False
print(bool([]))-->False

isinstance() #функция для проверки соответствия типа объекта какому-либо типу данных
print(isinstance(3, int))-->True
print(isinstance(3.5, float))-->True
print(isinstance('Beegeek', str))-->True
print(isinstance([1, 2, 3], list))-->True
print(isinstance(True, bool)-->True
print(isinstance(3.5, int))-->False
print(isinstance('Beegeek', float))-->False

type()#function позволяющая получить tipe указанного в качестве аргумента объекта
print(type(3))--><class 'int'>
print(type(3.5))--><class 'float'>
print(type('Beegeek'))--><class 'str'>
print(type([1, 2, 3]))--><class 'list'>
print(type(True))--><class 'bool'>
print(type(None)--><class 'NoneType'>
s = "asdf"
print(type(s))--><class str>
print(type(int))--><class type>

if var is None:#Проверка на None 
if var == None:#Проверка на None, оператор "==" менее предпочтителен

print(None == None)-->True

#функции, не возвращающие значений, на самом деле возвращают значение None

print('*', end='') # печать символа без переноса на следующюю строку

a = [1, 2, 3]
print(*a)-->1 2 3


if (x=1):
    print(1)
elif (x=2):
    print(2)
else:
    print(3)

len('abcdef') --> 6
'\n' #символ перевода строк
'\t' #символ табуляции
# # комментарий
'''
multi-line comments
'''

while i < 5: # оператор выполняющий цикл пока выполняется устловие
a, b = input().split() # сохраняет и разделяет пользовательский ввод
break # завершает цикл
continue # переходит на следующий цикл
for i in 1, 2, 3, 4 # оператор для последовательности чисел, i пройдет по всем числам после in
for i in range(2, 15, 4) # числа от 2 до 14 с шагом 4

for
   break
else:

while
else: somethink # else после for при выходе с break или выход с while будет выполнено 

for
    for
        if
            break
    if # можно использовать если break не было

# LIST COMPREHENSION

a, b = (int(i) for i in input().split()) # для пременных
a = [int(i) for i in input().split()] # для списка


x = [-2, -1, 0, 1, 2]
y = [i*i for i in x]
print(y) --> [4, 1, 0, 1, 4]

y = [i*i for i in x if i > 0] # with if
print(y) --> [1, 4]


z = []
for x in range(3):
    for y in range(3):
        if y >= x:
            z.append((x, y))
#same as
z =[(x, y) for x in range(3) for y in range(3) if y >= x] --> [(0, 0), (0, 1), (0, 2), (1, 1), (1, 2), (2, 2)]


z =((x, y) for x in range(3) for y in range(3) if y >= x) # если круглые скобки
print(z) --> generator object
print(next(z)) --> (0, 0)
print(next(z)) --> (0, 1)




# STRING

#преобразование в строку
a = len(input())*60
print(str(a//100)+' р. '+str(a%100)+' коп.')

# строки не изменяемы
genome = 'ATTG'
for c in genome:
    print(c)   # проход по строке

#f string
print(f'genome = {gemome}')--> genome = ATTG

genome = 'ATTG'
print(genome.count('T')) # считает сколько T в genome 

s='aTGcc' p='cc'
s.title()#all first simbol is big
s.upper() --> 'ATGCC'
s.lower() --> 'atgcc'
s.count(p) --> 1 # количество не пересекающихся вхождений, s.count(p, 3, 4) - 3 and 4 is position for search
s.find(p) --> 3 #retun only first position of simbols or -1, s.find(p, 3, 5) -3 and 5 is position for seaech
s.rfind(p)#см выше, только проверка идет справа
s.find('A') --> -1 #  не входит
if 'TG' in s:-->True #проверка вхождения в строку
s.replace('c', 'C') --> 'aTGCC'# s.replace ('c', 'C', 2) - max 2 first replace
s.index("TG")-->1 #index of first вхождения or ValueError
s.startswith("The man in black") # проверка начинается ли строка с данного набора символов, функция может принемать кортеж
s.endswith(".png")# см. выше, только проверяет окончание строки
s.split() # разделение по пробелу или заданному символу
s.strip() # clear simbols("\t", " ")
s.rstrip()# clear right side
s.lstrip()# clear left side
s.isalpha()# строка состоит только из букв
s.isdigit()# проверяет состоит ли строка только из цифр
s.rjust(10, '0' ) #делает строку равную длинне 10, а свободное место заполняет '0' или пробелами по дефолту
s.ljust(10) # см выше, два символа для заполнения передовать нельзя

s = 'agTtcAGtc'
genome.upper().count('gt'.upper()) --> 2 # с начала поднимает s, потом поиск поднятого gt

w ='Ivanov Ivon Ivanovich'
w = ','.join.(w.split())-->'Ivanov,Ivan,Ivanovich'

x = r"hello\nworld" #raw
print(x)-->hello\nworld

#.format()
template = '{} is the capital of {}.'
print(template.format("London", "Great Britain"))
template = '{1} is the capital of {0}.' #выбираем порядок
print(template.format("London", "Great Britain"))
template = '{capital} is the capital of {country}.' #выбираем порядок
print(template.format(capital="London", coutnry="Great Britain"))

import requests
template = "Response from {0.url} with code {0.status_code}."
res = requests.get("https://docs.python.org/3.5/")
print(template.format(res))

from random import random
x = random
print("{:.3}".format(x)) # output onli first three simbols after dot
# SLICING

dna = 'ATTCGGAGCT'
dna[1] --> 'T'
dna[1:4] --> 'TTC'
dna[:4] --> 'ATTC'
dna[4:] --> 'GGTAGCT'
dna[1:-1] --> 'TTCGGAGC'
dna[1:-1:2] --> 'TCGG'
dna[::-1] --> 'TCGAGGCTTA'

# СПИСКИ LIST
students = [] # пустой список
students = ['olya', 'seriy', 'pasha'] # заполненный список
for student in students:
   print("hello, " + student + "!")

# можно явно исменять список: 
students[0] = 'Olya'
students += ['Katya'] или students.append('Katya') # students += 'Katya' прибавит 5 элементов в список
list1 = list2 + list3 # сложение списков не путать с append
list.extend(list2) #сложение списков
students.insets(1, 'Boris') # вставляет элемент между 0 и 1 элементами
students.remove('Boris') # удаляет первое вхождение элемента 'Boris'
del students[0] # удаляет нулевой элемент
----
numbers = [10, 20, 30, 40]
del numbers[0:6]
print(numbers)-->[]#out of range не наступает
-------
list.pop([i]) # Удаляет i-ый элемент и возвращает его. Если индекс не указан, удаляется последний элемент
list.index(x, [start [, end]]) # Возвращает положение первого элемента со значением x (при этом поиск ведется от start до end)
list.count(x) # Возвращает количество элементов со значением x
list.copy() # Поверхностная копия списка
list.clear() # Очищает список
list.reverse() # инвертирует порядок следования значений в списке, то есть меняет его на противоположный
list.split() # разбивает строку на слова, используя в качестве разделителя последовательность пробельных символов, символ табуляции (\t) или символ новой строки (\n)
list.join() # собирает строку из элементов списка, используя в качестве разделителя строку, к которой применяется метод.

numbers = [4, 8, 12, 16, 34, 56, 100]
numbers[1:4] = [20, 24, 28]
print(numbers)-->[4, 20, 24, 28, 34, 56, 100]

#list copy
letters = ['a', 'b', 'c', 'd']
new_letters1 = letters.copy()
new_letters2 = letters[:]
new_letters3 = list(letters)

#max and min
words = ['xyz', 'zara', 'beegeek']
print(max(words))-->zara

list1 = [[1, 7, 12, 0, 9, 100], [1, 7, 90], [1, 10]]
list2 = [['a', 'b'], ['a'], ['d', 'p', 'q']]
print(min(list1))-->[1, 7, 12, 0, 9, 100]
print(max(list1))-->[1, 10]
print(min(list2))-->['a']
print(max(list2))-->['d', 'p', 'q']

# поиск элементов в списке
if 'ivan' in students:
   print('ivan is here')

if 'ivan' not in students:
   print ('ivan is out')

ind = students.index('Sasha') # возвращает индекс элемента в списке или ошибку

# сортировка

sorted_students = sorted(students) # не меняет изначальный список
student.sort() # меняет изначальный список
min() , max() # выводит максимальный и мин элемент (если элементы сравнимы)

students.reverse() или students[::-1] # переворачивает список
reversed(students)  # тоже но без изменения изначального списка

# создание списков
a = [] 
a = [1, 3, 5]
b = a // ссылка будет идти на один и тотже объект
a = [0] * 5 --> [0, 0, 0, 0, 0]  
a = [0 for i in range(5)] --> [0, 0, 0, 0, 0]
a = [i * i for i in range(5)] --> [0, 1, 4, 9, 16]

# двумерные списки
a = [[1,2],[3,4]]
a = [1][1] --> 4

my_list = ['Python', [10, 20, 30], ['Beegeek', 'Stepik!']]
print(my_list[2][-1][-1])-->!

a = [[0] * m for i in  range(n)] 
b = [[0 for j in range(m)] for i in range(n)] #same as
c = [[0] * m for _ in range(n)] #same as, можно ставить "_" если i не будет использована
d = [[0] * m ] * n # !!!! так нельзя, ссылка будет одна и таже

# КОРТЕЖИ(TUPLE)

# не изменяемы, быстрее чем списки, можно использовать в качестве ключей словаря,
#  удобно если зотим сделать что-то не изменяемое
# не имеют метода index, но имеют in
# Кортежи поддерживают:
# доступ к элементу по индексу (только для получения значений элементов);
# методы, в частности index(), count();
# встроенные функции, в частности len(), sum(), min() и max();
# срезы;
# оператор принадлежности in;
# операторы конкатенации (+) и повторения (*).

info = ('a', 0, False, (4, 5, 6), [])
g = (5) # это не кортеж
g = (5,) # это кортеж
g = () # пустой картеж
info[3:4] # срезы в кортежах это новый кортеж
g =([1, 3]) # списки внутри 

#list to tuple
str_list = ['один', 'два', 'три']
str_tuple = tuple(str_list)
print(str_tuple)-->('один', 'два', 'три')
str_list = list(str_tuple)
print(str_list)-->['один', 'два', 'три'] # tuple to list

# проверка на пустоту
tuples = [(), (), ('',), ('a', 'b'), (), ('a', 'b', 'c'), (1,), (), (), ('d',), ('', ''), ()]
non_empty_tuples = [i for i in tuples if len(i)>0]


is_target_node = False
node = 'Node1'
if (node == 'Node1' or node == 'Node2' or node == 'Node3')
    is_target_node = True
# сократим-->
node = 'Node1'
is_target_node = (node == 'Node1' or node == 'Node2' or node == 'Node3')
# сократим используя кортеж
node = 'Node1'
is_target_node = node in ('Node1', 'Node2', 'Node3')

# присваивание кортежу
f, s, *c, l = [1, 2, 3, 4, 5, 6, 7]  # *c--> [3, 4, 5, 6]

# передача dict to function argument
d = {'a': 1, 'b': 2}
def foo(a, b):
    pass
foo(**d)

# ФУНКЦИИ

def f(n):
    return n * 10 + 5 # Функция объявляется в начале программы

def min(*a): # Функция с произвольным количеством параметров
def my_range(start, stop, step = 1): # Функция с заданными параметрами

# ПЕРЕДАЧА АРГУМЕНТОВ В ФУНКЦИЮ

def printab(a, b):
    print(a)
    print(b)

printab(10, 20)
printab(a=10, b=20)
lst=[10 ,20]
printab(*lst)
args = {'a': 10, 'b': 20}
printab(**args)

def foo(a, b=10): # b - значение по умолчанию если не задано
def foo(a=20, b): --> Error syntacsis

def foo(a, b ,*args):
foo(1, 2, 3, 4, 5) # можно передовать произвольное количество аргументов

def printab(a, b, **kwargs):
    print(a, b)
    for key in kwargs:
        print(key, kwargs[key])
printab(10, c=30, jimmi=123, b=20)

# порядок инициализирования аргументов
def function_name([positional_args,
                  [positional_args_with_default,
                  [*post_args_name,
                  [keyword_only_name,
                  [**kw_args_name]]]]]):
def printab(a, b=10, *args, c=10, d, **kwargs):
    print(a, b, c, d)
print(15, d=15)-->15 10 10 15

# GLOBAL VARIABLE

ok_status = True
vowels = ["a", "u", "i", "e", "o"]
def check(word):
    global ok_status # использование не локальной переменной функции, а глобальной
    for vowel in vowels:
        if vowerl in word:
            return = False
    ok_status = False
    return False

#bild in - встроенное пространство имен, внутри него файл example.py c Глобальной областью видимости (global), внутри функций локальная область видимости (local)

# NONELOCAL VARIABLE

def f():
    ok_status = True
    def t():
        nonlocal ok_status #идет обращение на уровень(или несколько(пока не найдет нужную переменную)) 
        #выше локальной функции  
        ok_status = False
    s()
    print(ok_status)

f()-->False
print(ok_status) --> NameError #так как данной переменной нет в глобальном пространстве имен

#ЗАМЫКАНИЯ CLOSURE
#1
def main_func(name):
    n = name
    def inner_func():
        print('Hello', name)#что бы происходило замыкание необходимо использовать переменную из внешней функции
    
    return inner_func#мы передаем саму функцию а не ееё результат по этому без скобок
v = main_func('Vasya') #y ссылаеться на main_func('Vasya')
v() --> Hello Vasya
s = main_func('Sveta')
s() --> Hello Sveta
v() --> Hello Vasya #переменные сохраняются как в экземплярах класса это и называеться замыкание

#2
def adder(value):
    def inner(a):
        return (value + a)
    return inner
a2 = adder(2)
a2(5)-->7
a2(10)-->12
a5 = adder(5)
a5(10) -->15

#3
def counter():
    count = 0
    def inner():
        nonlocal count
        count += 1
        return count
    return inner
q = counter()
q() --> 1
q() --> 2
r = counter()
r() --> 1
r() --> 2
q() --> 3

#4
def averege_numbers():
    summa = 0
    count = 0
    def inner(number):
        nonlocal summa
        nonlocal count
        summa = summa + number
        count += 1

        return summa / count
    
    return inner
a = average_numbers()
a(100) -->100
a(200) -->150

#5
from datetime import datetime
def timer():
    start = datetime.now()
    def inner():
        return datetime.now() - start
    return inner
r = timer()
r() #веренет разницу между перевым и последним вызовом

#6 передача функциив качестве параметра
def add(a + b):
    return a + b
def counter(func):
    count = 0
    def inner(*args, **kwargs):
        nonlocal count
        count += 1
        print (f"Функция {func.__name__} вызывалась {count} раз")
        return func(*args, **Kwargs)
    return inner
q = counter(add)
q(10, 20) --> 30 Функция add вызывалась 1 раз
q(3, 4) --> 7 Функция add вызывалась 2 раз

#DECORATOR декораторы
def decorator(func):
    def inner(*args, **kwargs): # желательно всегда вставлять такие конструкции для параметров
        #в виде *args, **kwargs так как мы за ранее не знаем сколько будет параметров у функции 
        # которую мы будем декорировать
        print('start decorator...')
        func(*args, **kwargs)
        print('finish decorator...')

        return inner

def say(name, surname):
    print('hello', name, surname)

say = decorator(say)#now func working different
say('Vasya', 'Ivanov') --> start decorator...\n hello Vasya Ivanov \n finish decorator...

#2
def header(func):
    def inner(*args, **kwargs):
        print('<h1>')
        func(*args, **kwargs)
        print('</h1>')
        return inner

def table(func):
    def inner(*args, **kwargs):
        print('<table>')
        func(*args, **kwargs)
        print('</table>')
        return inner


def say(name, surname):
    print('hello', name, surname)

say = table(header(say))# обернули в 2 decorators
say('Vasya', 'Ivanov') --> <table><h1>hello Vasya Ivanov <\h1><\table>

#2a
#same as
@table
@header # '@table' and '@header' same as 'say = table(header(say))'
def say(name, surname):
    print('hello', name, surname)
say('Vasya', 'Ivanov') --> <table><h1>hello Vasya Ivanov <\h1><\table>



# МНОЖЕСТВА

s = set() # создание множества пустого
basket = {'apple', 'orange', 'apple'} # создание множества
print(basket) --> {'orange', apple'} # повторы исключаются
'orange' in basket --> True # проверка нахождения в множестве

# операции множеств

s.add(element)
s.remove(element) #вызывает ошибки при удалении если элемент отсутствует
s.discard(element) #не вызывает ошибок при удалении 
s.clear()

# СЛОВАРИ DICTIONARY

https://webdevblog.ru/kak-perebrat-slovar-v-python/

d = dict()
d = {}
d = {'a': 239, 10:100}
print(d['a']) # выведет ошибку если такого ключа нет в словаре
d[key] = value # присвоение нового значения ключу
d.get(key) # выдает либо значение либо None если ключа такого нет
del d[key] # удаление пары ключ и заначение


dict.clear() # очищает словарь.
dict.copy() # возвращает копию словаря.
dict.get(key[, default]) # возвращает значение ключа, но если его нет, не бросает исключение, а возвращает default (по умолчанию None).
dict.items() # возвращает пары (ключ, значение).
dict.keys() # возвращает ключи в словаре.
dict.pop(key[, default]) # удаляет ключ и возвращает значение. Если ключа нет, возвращает default (по умолчанию бросает исключение).
dict.popitem() # удаляет и возвращает пару (ключ, значение). Если словарь пуст, бросает исключение KeyError. Помните, что словари неупорядочены.
dict.setdefault(key[, default]) # возвращает значение ключа, но если его нет, не бросает исключение, а создает ключ с значением default (по умолчанию None).
dict.update([other]) # обновляет словарь, добавляя пары (ключ, значение) из other. Существующие ключи перезаписываются. Возвращает None (не новый словарь!).
dict.values() # возвращает значения в словаре
for key in sorted(d): # сортировка словаря по ключу


# перебор элементов словаря

d = {'C':14, 'A':12, 'T':9, 'G':18}
for key in d
    print(key, end=' ') --> G T A T
for key in d.keys():
   print(key, end=' ') --> G T A T
for value in d.values():
    print(value, end=' ') --> 18 14 12 9
for key, value in d.items():
    print(key, value, end='; ') --> G 18; C 14; A 12; T 9;

d['aaa'] = ['a', 'b'] # одному ключу может соответствовать список заначений


# WORK WITH FILE

# r (read) - open for read (default)
# w (write) - open for write, file clear
# a (append) - open for write, write in end
# b (binary) - open in binary mode
# t (text) - open in text mode
# r+ - open for read and write
# w+ - open for read adn write, file clear
f = open("test.txt", "rb")
x = f.read(5) # read first 5 simbols
y = f.read() # чтение всего оставшегося файла
print(repr(x)) # выводит строку со служебными символами ()
x = x.splitlines() # разделение на строки без спец сиволов и перенос в список
x = f.readline() # чтение построчно, так как целый фаил может занимать много места и чтение по строкам рациональнее
x = x.rstrip() # убирание символов с права от строки
f.close

f = open("text.txt")
for line in f:
    line = line.rstrip()
    print(repr(line))
    # в конце остается пустая строка
x = f.read()
print(repr(x)) -->'' # выводит посленюю строку
f.close

# ЧТЕНИЕ ИЗ ФАЙЛА

with open('text.txt', 'r') as inf:
    s1 = inf.readline()
    s2 = inf.readline()

inf.readline() # читает строку
inf.read() # читает весь текст
inf.readline().strip() # убирает спец символы в строке('\t', '\n')
inf.read().splitlines() # делит текст на строки

with open('text.txt', 'r') as inf:
    for line in inf:
        line = line.strip()
        print(line) # чтение всех строк в файле

 




import codecs# for reading cirilic and other
 
with codecs.open('file.txt', encoding='utf-8') as fin:
    line = next(fin)
    print type(line)
    print line.strip()

# ЗАПИСЬ В ФАЙЛ

with open('text.txt', 'w') as out:
    ouf.write('Some text\n') # \n oбязательна иначе переноса не будет
    ouf.write(str(25)) # перевод в строку обязателен

# write file

f = open("test.txt", "w") # если такого файла нет, то он будет создан
f.write("hello")
f.write("world") --> helloworld # для переноса нужет \n

lines = ["Line 1", "Line 2", "Line 3"]
contents = "\n".join(lines)
f.write(contents) # будет записано 3 строки

#append in file

f = open("test_append.txt", "a") # будет создан файл даже если он не создан
f.write("Hello")

f.close

# with - same as open-close

with open("text.txt") as f, open("text_copy.txt", "w") as w:
    for line in f:
        w.write(line) # copy in text_copy
        line = line.rstrip()
        print(line)

f.close


# МОДУЛИ

# имя модуля - это имя файла без расширения
import my_module # импорт модуля
my_module.foo() # использование функции из импортированного модуля

from my_module import foo
foo() # импорт одной функции из модуля

from my_module import *
foo() # импорт всех функций

from my_module import foo as my_foo
my_foo() # импор функции из модуля и назначение ей особого имени

# Модуль os
os.path.join('.', 'dirname', 'filename.txt') # подключаемый модуль позволяющий 
# переделывать путь к файлу в разных ОС --> './dirname/filename.txt' или '.\dirname\filename.txt'
os.path.dirname(path) # возвращает имя директории пути path
os.path.abspath(path) # возвращает нормализованный абсолютный путь.
__file__ # возвращает путь к файлу
print(os.path.dirname(os.path.abspath(__file__))) # выведет один и тот же путь как из интерпритатора
# так и из среды разработки


# Модуль sys показывает список аргументов командной строки
# запуск через cmd 
python file.py
import sys
print(len(sys.argv)) --> 1 # показывает что программа запущенна с одним аргументом (file.py)
print(sys.argv) --> file.py

# Модуль subprocess может запускать внешние процессы с параметрами
subprocess.call(["python", "-h"])

subprocess.call(args, *, stdin=None, stdout=None, stderr=None, shell=False, timeout=None) # можно назначить stdout и тогда вывод будет осуществлен в фаил, а не командную строку

# Установка библиотек

# после установки miniconda с галочкой PATH
# cmd от админа
conda install requests # установка библиотеки для работы в интернете

# Модуль requests может взамодействовать с сайтами 
import requests
r = requests.get('http://example.com') 
print(r.text) # выведет текст сайта
print(r.status_code)
print(r.url)
print(r.headers['Content-Type'])

from requests import get
get('https://stepic.org/favicon.ico').headers['Server'] # show server name



# Библиотека NumPy # работа с числовыми массивами
conda install numpy
a = array([2, 3, 4]) # создание одномерного массива, массивы могут быть только одного типа
a.ndim --> 1 # размерность массива
a.shape--> (1, 3) # 1строка 3 столбца
z = zeros((3,2)) # заполнение массива 3 на 2 нулями
arange(10, 30, 5) # генерирование массива от 10 до 30 с шагом 5
linspace(0, 2, 9) # генерация массива от 0 до 2 (ключительно) в размере 9 точек
b = arrage(12).reshape(4, 3) # превращение одноменого массива в 4 на 3

# сложение массивов
a = array([10, 20, 30])
b = arange(3)
print(a) --> [10 20 30]
print(b) --> [0 1 2]
print(a + b) --> [10 21 32] # сложение и вычитание происходит поэлементно
print(a**2)--> [100 400 900]
print(2*sin(a)) --> [-1.08 1.82 -1.97]
print(a<20) --> [True Folse Folse]



# Библтотека matplotlib # построение графиков
conda install matplotlib



# УСЛОВИЯ
if foo == True:
...
if boo == False:
# сократим
if foo:
...
if not boo:


if len(value) > 0:
# сократим
if len(value):
# сократим
if value !=[]: # '' для строк, {} для словарей, set() для множеств, () для кортежей
# сократим
if value:

# ЦИКЛЫ
# по циклу лучше проходить не используя индекс, а проходя по значению

# если требуется иметь доступ к индексу и значению то стоит использовать функцию enumerate
my_list = ['Node1', 'Node2', 'Node3']
for i, value in enumerate(my_list):
    print(i, value)
# enumerate превращает список в кортеж, где по два элемента (( , ),( , ))


# функция формат {}.format (потом поискать в интернете)


# FUNCTION .join

l = ['a', 'b' , 'c']
s = ''
for value in l:
    s += value + ', '
print(s)
***
l = ['a', 'b' , 'c']
print(', '.join(l))
# если требуется преобразование
l = [1, 2 , 3]
print(', '.join(str(x) for x in l))


# так как значение по умолчанию для функции вычисляется один раз, не стоит использовать изменяющиеся обьекты (списки, словари)
def f(x, l=[]):
    l.append(x)
    return l
print(f(1)) -->[1]
print(f(2)) -->[1, 2]
print(f(3)) -->[1, 2, 3]
***
def f(x, l=None):
    if l is None:
        l = []
    l.append(x)
    return l
print(f(1)) -->[1]
print(f(2)) -->[2]
print(f(3)) -->[3]

# формирование словаря

def foo()
    somethink
cache = {x: foo(x) for x in range(-100, 100)}

# при генерации в круглых скобках производится экономия памяти

l = [...]
v1 = [x for x in l if x % 2 == 0]
v2 = (x for x in l if x % 2 == 0)

# ИДЕНТИФИКАТОР ОБЪЕКТА

x = [1, 2, 3]
print(id(x)) --->12345
print(id([1, 2, 3])) --->44385

# ОПЕРАТОР is проверяет ссылаются ли переменные на один и тотже обьект
x = [1, 2, 3]
y = x
y is x ---> True
y is [1, 2, 3] ---> False
x is None # проверяет объект на пустоту

type(x) #показывает тит объекта

Immutable                          Mutable
int                                list
float                              dict
complex(комплексные числа)         set
bool
tuple(кортеж)
str
frozenset(не изменяемое множество)

def от define(определим)

# +РАБОТА ФУНКЦИИ

a = []
def foo(arg1, arg2):
  a.append("foo")
foo(a.append("arg1"), a.append("arg2"))
print(a) --> ['arg1', 'arg2', 'foo']

# СТЕК ВЫЗОВА

x = [1, 2, 3]
print(x.pop())-->3
print(x)-->[1, 2]
print(x.append(4))-->None
print(x)-->[1, 2, 4]


# CLASSES

class MyClass:
    a = 10
    def func(self):
        print('Hello')
    def drive():
        print('Go Go Go')
print(MyClass.a) # MyClass.a атрибут класса MyClass
print(MyClass.func) #  MyClass.func атрибут класса MyClass
# в отличии от функций тело класса исполняется в момент определения самого класса и за ним закрепляется определенный namespace
print(MyClass.__dict__) # show attributes and other info of class
print(getattr(MyClass, 'a', 100))--> 10 #show attribute 'a' (quotes is necessary), 100 - return value, if attribute 'a' does not exist(не существует)
#100 - not necessary attrebute
MyClass.b = 'something' #in MyClass added attribute 'b' wint value 'something'
setattr(MyClass, 'c', 200) #in Myclass added attribute 'c' with value 200
del MyClass.a #deleting attribute 'a'
delattr(MyClass, 'b') #deleting attribute 'b'
#functions
MyClass.drive() --> Go Go Go #скобки это оператор вызова
MyClass.drive-->#show link
getattr(MyClass, 'drive')-->#show link
getattr(MyClass, 'drive')()-->Go Go Go
hasattr(MyClass, 'name')-->True/False

# OBJECT OF CLASS

class MyClass:
    a = 10
    def func(self): #self - общепринятое название(можно заменить на любое другое),
        #when instance run func of class he вставляет youself за место self
        #по этому MyClass.func - запуститься, а a.func - выдаст ошибку так как будет передан аргумен в виде instance
        print('Hello')
x = MyClass() # x is instance(экземпляр) of class MyClass. MyClass() it's constructor of class MyClass
print(type(x))
print(type(MyClass))
b = MyClass()
print(MyClass.__dict__) #show all attributes
print(b.__dict__ ) #show empty list
b.a = 20
print(b.__dict__) #show attribute 'a'
del b.a 
print(b.a)-->10 #if we don't have attribute in instance of class, Python search attribute in class and parents




class Counter:
    pass # when hollow(empty) class
Counter -->class object
x = Counter() # x is instant object
x.count = 0
x.count += 1


class Counter:
    def __init__(self):  # a function __init__ принимает ещё не существующий instance(экземпляр) self
        self.count = 0 # к ещё не существующему instance, add attribute
Counter
x = Counter()
print(x.conut) --> 0
x.count += 1


class Counter:
    def __init__(self, start = 0):   
        self.count = start 
Counter
x1 = Counter(10) # аргумент 10 встает after self in def __init__
x = Counter()
print(x.conut) --> 0
x.count += 1

# METHOD
class Cat:
    def voice():
        print('mao')
bob = Cat()
bob.voice()--> #вызовет ошибку так как в def voice() нет аргумента, а показано что был передан один аргумент
print(Cat.voice) #покажет что это функция
print(Cat.voice) #покажет что это метод
#метод это таже функция, но у класса, метод привязан к конкретному обьекту, а функция не с кем не связана
#в функцию в классе(в метод), при вызове её от экземпляра передается сам экземпляр 'voice(bob)'

class Cat:
    def voice(*args): # *args - any quantity of arguments
        print('mao', *args)
jim = Cat()
jim.voice()-->mao (<__main__.Cat Object at 0x5234534534>,)#main - this file, 0x124232532 - place in storege


#__init__
#чтобы не add attribute thought func, we can add attribute when initing instance
class Counter:
    def __init__(self):  
        self.count = 0
    def inc(self):
        self.count += 1
    def reset(self):
        self.count = 0
x = Counter()#in this moment adding attribute count in instance, хотя функция __init__ на прямую не вызывалась
#если в __init__ добавить больше арибутов (__init__(self, name)) то получим конструктор
x.inc --> 1
print(x.count)
Counter.inc(x) -->2 # Тоже самое что и x.inc строчкой выше (Bound Method(связанный метод))
print(x.count)
x.reset()-->0
print(x.count)

#dry (don't repeat youself)
class Point:
    list_points = []
    def __init__(self, x, y):
        self.change(x, y)
        Point.list_pints.append(self) #для обращения к аттрибутам класса необходими указывать сласс
        #даже если функция внутри класса
    def change(self, x, y):
        self.x = x
        self.y = y
    def go_home(self):
        self.change(0, 0)

#моносостояние for instance
#when при changing or adding attribute in one instance происходит changing all instance 
class Cat:
    def __shared_attr = {
        'breed': 'pers'
        'color': 'black'
    }
    def __init__(self):
        self.__dict__ = __shared_attr
a = Cat()
b = Cat()
a.breed = 'pers'
print(b.bread)--> pesr

#public protected privated attr and methods
#public _protected __privated
#_protected - никак не защищает "_" просто общепринятое обозначение
class BankAccount:

    def __init__(self, name, balance, passport):
        self.__name = name
        self.__balance = balance
        self.__passport = passport
    
    def print_public_data(self):
        self.__print_pvivate_data()

    def print_protected_data(self):
        print(self.__name, self.__balance, self.__passport)

account1 = BankAccount()
account1.__name -->Error
account1.__print_private_data() --> Error
account1.print_public_data #так можно
print(dir(account1)) #show all attr and private attr
account1._BankAccount.__print_private_data() #и так он показывает защищенные атрибуты
#по сути Python не защищает ничего

#property getter setter delete
class BankAccount:

    def __init__(self, name, balance):
        self.name = name
        self.__balance = balance
    
    def get_balance(self):
        return self.__balance

    def set_balance(self, value):
        if not isinstance(value, (int, float)):
            raise ValueError('Баланс должен быть числом')
        self.__balance = values
    
    def delete_balance(self):
        del self.__balance
    
    balance = property(fget = get_balance, fset = set_balance, fdel = delete_balance)
    # short name for using func
a = BankAccount()
a.balance #вызов get_balance
a.balance = 100 #вызов set_balance
del a.balance #вызов delete_balance

#decorator property
#избавлеяет от двойной функциональности
class BankAccount:

    def __init__(self, name, balance):
        self.name = name
        self.__balance = balance
    
    @property #1 превращаем нашу функцию в свойство путем декорирования
    def my_balance(self):#1 change name to my_balance
        return self.__balance

    @my_balance.setter #2 property of my_balance (то что был getterom (#1))
    def my_balance(self, value):
        if not isinstance(value, (int, float)):
            raise ValueError('Баланс должен быть числом')
        self.__balance = value
    
    @my_balance.deleter
    def my_balance(self):
        del self.__balance

p = BankAccount('Tod', 900)
p.my_balance --> 900 # скобки не нужны так как это свойства  
p.my_balance = 901
p.my_balance --> 901
del p.my_balance
p.my_balance --> Error

#2
class Money():
    def __init__(self, dollars, cents):
        self.total_cents = dollars * 100 + cents

    @property
    def dollars(self):
        return self.total_cents//100

    @dollars.setter 
    def dollars(self, dollars):
        if isinstance(dollars, int) and dollars >= 0:
            self.total_cents = dollars*100 + self.total_cents%100
        else: print('Error dollars')

    @property
    def cents(self):
        return self.total_cents%100

    @cents.setter 
    def cents(self, cents):
        if isinstance(cents, int) and 100 > cents >= 0:
            self.total_cents = self.total_cents//100*100 + cents
        else: print('Error cents')

    def __str__(self): # __str__ change return of instance
        return f"Ваше состояние составляет {self.total_cents//100} долларов {self.total_cents%100} центов"
Bill = Money(101, 99)
print(Bill)  --> Ваше состояние составляет 101 долларов 99 центов
print(Bill.dollars, Bill.cents)  --> 101 99

#Вычисляемые Property
class Square:
    def __init__(self, s):
        self.__side = s
        self.__area = None
    
    @property
    def side(self):
        return self.__side
    
    @side.setter
    def side(self, value):
        self.__side = values
        self.__area = None #when change side, area change to None
    
    @property #for more comfortable call to area do it to property
    def area(self):
        if self.__area is None: # что бы не вычеслять area каждый раз, а только в первый раз
            print('calculate area')
            self.__area = __side**2
        return self.__area
a = Square(5)
a.area -->calculating area 25
a.area --> 25
a.side = 6
a.area -->calculating area 36
a.area -->36

#staticmethod and classmethod
class Example:
    def hello():
        print(hello) #работае только при вызове от класса
    
    def instance_hello(self):
        print(f'instance_hello {self}') #работает только при вызове от instance

    @staticmethod
    def static_hello():
        print(f'static_hello') #работает ото всех
    
    @classmethod
    def class_hello(cls): #работает ото всех, cls - class, и от instance и от class в cls попадает class
        print(f'class_hello {cls}')

Example.hello() --> hello
a = Example
a.hello() --> Error
Example.instance_hello() --> Error
a.instance_hello() --> instance_hello < a >
Example.static_hello() --> static_hello
a.static_hello() --> static_hello
Example.class_hello()--> class_hello <class Example>
a.class_hello()--> class_hello <class Example>

#способы обращения к переменным/методам класса
#1 если два файла в одной папке
import file1
Example.method1()
2#
class DepatrtmentIT:
    PYTHON_DEV = 4
    GO_DEV = 3
    REACT_DEV =2
    def info(self):
        print(self.PYTHON_DEV, self.GO_DEV, self.REACT_DEV)
    def info2(self):
        print(DepatrtmentIT.PYTHON_DEV, DepatrtmentIT.GO_DEV, DepatrtmentIT.REACT_DEV)
    @property
    def info_prop(self):
        print(self.PYTHON_DEV, self.GO_DEV, self.REACT_DEV)
    @classmethod
    def info_class(cls):
        print(cls.PYTHON_DEV, cls.GO_DEV, cls.REACT_DEV)
    @staticmethod
    def info_static():
        print(DepatrtmentIT.PYTHON_DEV, DepatrtmentIT.GO_DEV, DepatrtmentIT.REACT_DEV)

#включения сеттора при инициализации
from string import digit #digit - it is just list of digit
class User:

    def __init__(self, login, password):#так как сеттер и переменная называются одинаково
        # во время инициализации происходит проверка пароля через сеттер
        self.login = login
        self.password = password
    @property
    def password(self):
        print('getter called')
        return self.password
    @staticmethod
    def is_include_number(password):#just checing(проверка) to having digit in pass
        for digit in didgits:
            if digit in password:
                return True
        return False
    @password.setter
    def password(self, value):
        print('setter called')
        if not isinstance(value, str):
            raise TypeError('Password not the string')
        if len(value)<4:
            raise ValueError('Pass is too short, need min 4 simbols')
        if len(value)>12:
            raise ValueError('Pass is too long, need max 12 simbols')    
        if not User.is_include_number(value):
    
#__call__
# '()' - оперератор вызова
#7 видов вызываемых(callable) объектов в Python
# 1 вызываемые функции len() abs() int() и т д
# 2 callable method a = [1, 2, 3] a.sort()
# 3 собственные функции def
# 4 classes Cat()
# 5 instance is not callable, but we might inicialising method __call__
class Cat:
    def __call__(self, *args, **kwargs):
        print('may')
bob = Car()
print(callable(bob))-->True
bob()--> 'may'
# 6 method of classes
# 7 function-generator
def f():
    n = 0
    while True:
        yield n
        n += 1
print(callable(f))--> True

#__call__
#избавляемся от замыкания
class Counter:
    def __init__(self):
        self.counter = 0
        self.summa = 0
        sefl.length = 0
    def __call__(self, *args, **kwargs):
        self.counter += 1
        self.summa += sum(args)
        self.length = += len(args)
        print(f'Наш экземпляр вызывался {self.counter} раз')
    def averege(self):
        return self.summa /self.length
r = Counter()
r(2, 4, 5, 6) # тепер можно вызавать таким образом instance
r.average()
#избавляемся от декорирования
from time import perf_counter
class Timer:
    def __init__(self, func):
        self.fn = func
    def __call__(self, *args, **kwargs):
        start = perf_counter()
        print(f'call function {self.fn.__name__}')
        result = self.fn(*args, **kwargs)
        finish = pers_counter()
        print(f'функция отработала за {finish - start}')
        return result
#@Timer    
def fact(n):
    pr = 1
    for i in range(1, n + 1):
        pr *= 1
    return pr

def fib(n):
    if n<=2:
        return 1
    return fib(n-1) + fib(n-2)

fact = Timer(fact) #либо можно было поставить декоратор @Timer
fact(7)-->5040

fib = Timer(fib)
fib(20)
Timer(fib)(7) #декорируем и сразу вызываем с аргументом, сама фунция фиб здесь не задекорирована, задекорирован только ее вызов

# VARIABLE OF CLASS

class Song:
    tags = []
    def __init__(self, artist, song):
        self.artist = artist
        self.song = song
        #self.tags = []
    def add_tags(self, *args):
        self.tags.extend(args) # extend() - тоже самое что и append(), но может добавлять несколько элементов
song1 = Song("Shakey", "Roll")
song1.add_tags("Americana", "Country")
song2 = Song ("Neuromonah", "Holodno")
song2.add_tags("Russian", "Drum")
print(song2.tags) --> "Americana" "Country" "Russian" "Drum" # все добавилось в tags = [] так как не объявлен атрибут self.tegs и интерпритатор ищет его в классе
таково бы не случилось если ракоментировать self.tags = [] и закоментировать tags = []
#MAGIC METHOD
#__repr__ and __str__
class Lion():
    def __init__(self, name):
        self.name = name
    def __repr__(self):#заменяет обычное отображение класса в том числе и для разработчиков, если нет
        return f'The object Lion - {self.name}' 
    def __str__(self):#заменяет обычное отображение класса в print() and str()
        return f'Lion - {self.name}'
a = Lion('alex')
a #__repr__
str(a) #__str__
print(a) #__str__

#__len__ and __abs__
class Otrezok:
    def __init__(self, point1, point2):
        self.x1 = point1
        self.x2 = point2

    def __len__(self): #setting for comand 'len()'
        return abs(self)

    def __abs__(self):# setting for comand 'abs()'
        return abs(self.x2 - self.x1)

a = Otrezok(4, 8)
len(a) --> 4 #show 4, таким образом мы настроили work function len of our class


#__add__,__radd__,__mul__,__rmul__,__sub__,,__truediv__
#сложение, умножение, вычитание, деление. #r - тажа операция, но с заменой слагаемых/мнжителей местами
class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def __add__(self, other):
        print('__add__ calc')
        if isinstance(other, BancAccount): #проверяем если складываем с такимже классом
            return self.balance + other.balance
        if isinstance(other, (int, float)):
            return self.balance + other
        raise NotImplemented
    
    def __radd__(self, other):
        print('__radd__ call')
        return self+other
r = BankAccount('Ivan', 200)
r+12 #run comand r.__add__(12)
12+r #run comand r.__radd__(12) #с начала Python пытаеться вызвать команду __add__ и когда это не получаеться он меняет слогаемые местами и вызывает команду __radd__

#2 передача обьекта а не числа
class BankAccount:
    def __init__(self, name, balance):
        print('New obj init')
        self.name = name
        self.balance = balance

    def __add__(self, other):
        print('__add__ calc')
        if isinstance(other, BancAccount): 
            return self.balance + other.balance
        if isinstance(other, (int, float)):
            return BankAccount(self.name, self.balance + other) #возвращаемь новый созданный обьект
        raise NotImplemented
t = BankAccount('Ivan', 200)
d = t + 30 #now we able to do so. 'd' is new obj

#методы сравнения
# __eq__ == (equal)
# __ne__ != (not equal)
# __lt__ < (less than)
# __le__ <= (less euqal)
# __gt__ >
# __ge__ >=

class Rectangle:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    @property
    def area(self):
        return self.a * self.b
    
    def __eq__(self, other):
        if isinstance(other, Rectangle):
            return self.area == other.area
        
    def __lt__(self, other):
        if isinstance(other, Rectangle):
            return self.area < other.area

    def __le__(self, other):
        return self.__eq__(other) or self.__lt__(other)

a = Rectangle(1, 2)
b = Rectangle(1, 2)
a == b --> True
b > a --> True #хоть мы и не делали __gt__, Python пробует перевернуть a < b и такая функция есть
#но нужно что бы второй аргумент тоже имел функцию a.__lt__(b).
b != a --> False # not (b == a) , __ne__ можно не реализовывать
b >= a --> True # a <= b 



#__eq__ and __hash__
#если переопределяем eq то нужно переопределить и hash, так как по умолчанию hesh от ссылки, а ты её переопределяем
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __eq__(self, other):
        return isinstance(other, Point) and self.x == other.x and self.y = other.y
    def __hash__(self):
        return hash((self.x, self.y))
p1 = Point(3, 4)
p2 = Point(3, 4)
p3 = Point(6, 7)
p1 == p2 --> True
hash(p1) == hash(p2) --> True
p1 == p3 --> False
hash(p1) == hash(p3) -->False

#__bool__
class Point:
    class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __len__(self): #так как bool([])-->False и т.д. Bool ориентируеться по len, и парой len достаточно. Если bool не определен то он идет в len
        return abs(self.x - self.y)
    def __bool__(self):
        return self.x != 0 or self.y != 0
bool(Point(3, 4))-->True 
bool(Point(0, 0))-->False

# НАСЛЕДОВАНИЕ CLASS

class DerivedClassName (Base1, Base2, Base3): # Base1..3 классы от которых идет наследование


class MyList(list):
    def even_lenght(self):
        return len(self) % 2 == 0
x = MyList()
print(x)--> []
x.extend([1, 2, 3, 4, 5])
print(x)--> [1, 2, 3, 4, 5]
print(x.even_lenght()) -->False
x.append(6)
print(x.even_lenght()) -->True  # def __repr__(self): #от representation print смотрит в классе как показать что либо (урок 1.6.3)


class D: pass
class E: pass
class B(D, E): pass
class C: pass
class A(B, C): pass
issubclass(A, A) --> True # every class heir(наследник) is himself. issubclass is function for проверки является ли first argument heir of second argument
issubclass(C, D) --> False 
issubclass(A, D) --> True
issubclass(C, object) --> True # class object ancestor(предок) for every classes
issubclass(object, С) --> False # class object don't have parents
x = A()
isinstance(x, A) --> True # isinstance проверяет является ли объект экземпляром какого-либо класса
isinstance(x, B) --> True
isinstance(x, object) --> True
isinstance(x, str) --> False
print(A.mro()) # от method resolution order, показывает порядок перебора классов в множественном наследовании 


class EvenLengthMixin:
    def even_length(self):
        return len(self) % 2 == 0
class MyList(list, EvenLengthMixin):
    def pop(self):
        x = super(MyList, self).pop() #функция супер застовляет искать функцию в предках MyList исключая MyList, тоже самое list.pop(self)
        print("Last valut is ", x)
        return x
ml = MyList([1, 2, 4, 17])
z = ml.pop() --> Last value is 17
print(z) --> 17
print(ml) --> [1, 2, 4]


# EXCEPTIONS

try:                          # try ... except TypeError - catch Error (TypeError) and do somethink after except
    x = [1, 2, "hello", 7]
    x.sort
    print(x) 
except TypeError:
    print("Type Error :-(")
except ZeroDivisionError:
    print("ZeroDivisionError :-(") # we can make several exception 

print ("I can natch")
# if in function have error, then function return - None


def f(x, y):
    try:
        return x / y
    except (TypeError, ZeroDivisionError) as e: # catch in one exception two errors
        print(type(e)) # выводим параметры ошибки (и в строках ниже тоже)
        print(e)
        print(e.args)
    finally:  # блок finally запускается в любом случаи, была поймана ошибка или нет
        print("finally")
print(f(5, 0))


except:   #cath every errors
    print("Error :-(")

# MY EXCEPTIONS

def greet(name):
    if name[0].isupper():
        return "Hello,  " + name
    else:
        raise ValueError (name + " is inappropriate name") # is crate me exception

print(great("Anton"))
print(great("anton")) --> ValueError: anton in inappropriate name


# me can catch my exception
def greet(name):
    if name[0].isupper():
        return "Hello,  " + name
    else:
        raise ValueError (name + " is inappropriate name")

while True:
    try:
        name = input("Please enter you name: ")
        greeting = great(name)
        print(greeting)
    except ValueError:
        print("Please try again")
    else:
        break # if don't catch break


# if we wont see our Error_name, then we create own Error_class
class BadName(Exception): # Exception is main class all exceptions
    pass

def great(name):
    if mane[0].isupper():
        return "Hello, " + name
    else:
        raise BadName(name + " is inappropriate name")

print(great("Anton"))
print(great("anton"))--> BadName : antom is anapropriate name"



# IMPORT
(2.2.1)

#exceptions.py
class BadName(Exception):
    pass

def great(name):
    if mane[0].isupper():
        return "Hello, " + name
    else:
        raise BadName(name + " is inappropriate name")
print("Import is execution")

#import_lesson.py

import exceptions

print(exceptions.great("Students"))
-->
Import is execution # becouse import исполняется in time объявления



# что бы не исполнять не нужный код во время импорта в другой файл
# есть паттерн проверки по имени. Если прописать print(__name__) в файле и запустить из это го же файла 
# --> __main__


# fib.py
def fib(k):
    if k == 0 or k == 1:
        return 1
    else:
        return fib(k - 1) + fib(k -2)

if name == "__main__": # если  запуск из файла --> __main__
    print(__name__)
    print(fib(31)) # это строка исполняется очень долго и импорт её очень затратен

# import_lesson.py
import fib # если запуск из файла с импортом то имя будет fit и строки ниже if name == "__main__": не исполнятся


# большой урок 2.2.3 про import 
# 1) импорт исполняется один раз 
# 2) есть словать импорта куда всегда идет обращения, что бы не исполнять импорт 2 раза
# 3) если в словаре нет поиск идет по внешним библиотекам 

# IMPORT PART OF SOMETHINK
from exceptions import BadName, greet #импорт из файла exceptions.py  класса BadName и функции greet

from exceptions import BadName, greet as exc_greed # теперь в данном файле функция greed именнуется как exc_greed

from exceptions inport * # импортируются все имена exceptions.py, кроме имен начинающихся с "_" и не перечисленных в 
# __all__ если такая функция имеется

# exceptions.py
GREETING = "Hello"

class BadName(Exception):
    pass

def great(name):
    if mane[0].isupper():
        return GREETING + name
    else:
        raise BadName(name + " is inappropriate name")

__all__ = ["BadName", "greet"] # GREETING импортировано не будет

# PIP - Утилита pip позволит нам устанавливать пакеты из репозитория Python Package Index
pip --version
# или
pip3 --version


# ITERATOR

lst = [1, 2]
iterator = iter(lst)
print(next(iterator)) --> 1
print(next(iterator)) --> 2
print(next(iterator)) --> StopIteration


for i in lst:
    print(i)
# same as
it = iter(it)
while True:
    try:
        i = next(it)
        print(i)
    except StopIteration:
        break



# iterator in my_class
class RandomIterator:
    def __next__(self):
        return 0

x = RandomIterator()
print(next(x))



from random import random

class RandomIterator:
    def __init__(self, k):
        self.k = k
        self.i = 0

    def __next__(self):
        if self.i < self.k:
            self.i += 1
            return random
        else:
            raise StopIteration

x = RandomIterator(3)
print(next(x)) # next(x) эквивалентно x.__next__() 
print(next(x))
print(next(x))
print(next(x))--> StopIteration

# "for" in my_class
from random import random

class RandomIterator:
    def __iter__(self):
        return self

    def __init__(self, k):
        self.k = k
        self.i = 0

    def __next__(self):
        if self.i < self.k:
            self.i += 1
            return random
        else:
            raise StopIteration

for x in RandomIterator(10):
    print(x)

# "for" in my_class2
class DoubleElementListIterator:
    def __init__(self, lst):
        self.lst = lst
        self.i = 0
    def __next__(self):
        if self.i < len(self.lst):
            self.i += 2
            return self.lst[self.i-2], self.lst[self.i-1]
        else:
            raise StopIteration

class MyList(list)
    def __iter__(self): 
        return DoubleElementListIterator(self)

for pair in MyList([1, 2, 3, 4]): 
    print(pair)
#Метод __iter__() запускается один раз при создании экземпляра класса MyList и в этот момент 
# этот созданный экземпляр становится "итерируемым" (интерпретатор запоминает все, что ему нужно 
# для работы про этот объект). Дальше вы уже работаете с этим экземпляром и все что вы делаете, 
# в том числе итерируетесь по нему (вызываете метод next), связано именно с этим экземпляром. 
# При создании нового экземпляра __iter__() будет запущен еще раз, но этот вызов будет связан 
# именно с этим новым экземпляром и никак не повлияет на счетчики ранее созданных экземпляров.

# GENERATOR
# yield - это отложенное исполнение при этом не требующее next и iter

def semple_gen():
    print(1)
    yield 1
    print(2)
    # retunt "No more lements" - если вставить эту строку, то после return ничего читаться не будет,
    # будет брощена StopIteration: No more elements
    yield 2
    print (3)

gen = simple_gen()
x = next(gen)
print(x) --> 1
y = next(gen)
print(y) --> 2
z = next(gen) --> StopIteration




from random import random

def random_generator(k):
    for i in range(k):
        yeild random()
gen = random_generator(3)
for i in gen:
    print(i)




# MODULE OS

import os
import os.path

print(os.getcwd())# show used dirrectory interpritator
print(os.listdit.("Test")) # show files in derrectory "Test"
print(os.path.exists("file.py"))--> True/False # show exists(существует) file or folder
print(os.path.isfile("file.py"))--> True # is file or not
print(os.path.isdir("Test"))-->True # is dirrectory or nor
print(os.path.abspath("file.py")) # show absolutely way to file
os.chdir("2") # change dirrectory
os.chdir(r"C:\\Learning\Python\2\2.4.6\sample") # for windows  '\\' and 'r'

for current_dir, dirs, files in os.walk("."): # "." - is текущая dir
    print(current_dir, dirs, files) # show all dir and files

# MODULE SHUTIL

import shutil

shutil.copy("tests/test1.txt", "tests/test2.txt") # copy test1.txt in dir tests to test2.txt in dir tests
shutil.copytree("tests", "tests/tests") # copy folder "tests" to tests/tests


# FUNKTION map()
# map is itetable function
n, k = map(int, input().split()) #прогоняет список через нужную функцию
# same as
x = input().split()
n, k = (int(i) for i in x)

def addition(n): 
    return n + n  
numbers = (1, 2, 3, 4) 
result = map(addition, numbers) 
print(list(result))-->[2, 4, 6, 8]


numbers1 = [1, 2, 3] 
numbers2 = [4, 5, 6] 
result = map(lambda x, y: x + y, numbers1, numbers2) 
print(list(result)) --> [5, 7, 9]


def func(el1, el2): 
    return '%s|%s' % (el1, el2)
list(map(func, [1, 2], [3, 4, 5]))--> ['1|3', '2|4']

dict(map(lambda *args: args, [1, 2], [3, 4]))--> {1: 3, 2: 4} #удобное создание словаря


numbers = map(str, [1, 2, 3, 4, 5])
print(repr(" ".join(numbers)))
# FUNCTION filter

x = input().split()
xs = (int(i) for i in x)

def even(x):
    return x % 2 == 0 -->T/F

evens = filter(even, xs) # прогоняет list/cortage (xs) throw function (even), if even is True, element of xs append in evens
for i in evens:
    print(i)
# same as
evens = list(filter(even, xs)) # filter это итератор, если его поместить в list то он достанет все обьекты итератора (можно использовать если конечное число элементов и ест не много памяти)
print(evens)

# FUNKTION lambda

def identity(x):
    return x % 2 == 0
a = identity(x)
# сократим
a = lambda x: x % 2 == 0


print(lambda x: x + 1)(3)-->4


add_one = lambda x: x + 1
add_one(2) --> 3


x = input().split()
xs = (int(i) for i in x)
evens = list(filter(lambda x: x % 2 == 0, xs ))
print(evens)


x = [
    ("55555", "333", "666666"),
    ("7777777", "55555"),
    ("4444", "666666")
]
def length(name):
    return len(" ".join(name))
name_lengths = [length(name) for name in x]
print(name_lengths)
x.sort(key = length)
print(x)
# same as
x = [
    ("55555", "333", "666666"),
    ("7777777", "55555"),
    ("4444", "666666")
]
x.sort(key = lambda name: len(" ".join(name)))
print(x)

# LIB OPETATER

import operator as op

print(op.add(4, 5)) # сложение
print(op.mul(4, 5)) # умножение
print(op.contains([1, 2, 3, 4, 5], 6))-->False # проверяет наличия числа в контейнере

x = [1, 2, 3]
f = op.itemgetter(1) # выбран element with index 1 # f(x) == x[1]
print(f(x))-->2 # x[1]

x = {"123": "asfd"}
f = op.itemgetter("123")
pritn(f(x))

f = op.attrgetter("sort") #f(x) == s.sort
print(f([]))

x = [
    ("55555", "333", "Rosssum"),
    ("7777777", "curry"),
    ("4444", "backus")
]
x.sort(key = op.itemgetter(-1)) #sort by last element
print(x)


# LIB FUNCTOOLS
from functools import partial

x = int("1101", base=2)
print(x)-->13
#same as
int_2 = printab(int, base =2)
print(x) -->13


import operator as op
from functools import partial
x = [
    ("55555", "333", "Rosssum"),
    ("7777777", "curry"),
    ("4444", "backus")
]
sort_by_last = partial(list.sort, key=op.itemgetter(-1))
print(x)
#same as
sort_by_last(x) #при помощи функции partial функция sotr_by_last запоминает параметры, что их не нужно вводить снова
print(x)

y = ["abc", "cba", "abb"]
sort_by_last(y)
print(y)

# PEP8 AND DOCUMENTATION
# https://www.python.org/dev/peps/pep-0008/ - EN
# http://pythonworld.ru/osnovy/pep-8-rukovodstvo-po-napisaniyu-koda-na-python.html или http://defpython.ru/pep8 - RU


class my_class:
    """
    documentation of my_class
    """
    pass
print(my_class.__doc__) 


print(str.find.__doc__) # документация какой-либо функции

# MODULE RE РЕГУЛЯРНЫЕ ВЫРАЖЕНИЯ

import re


pattern = r"abc"  # r - raw значит читается как пишется
string = "abcd"
match_object = re.match(pattern, string) # проверяет начинается ли наша строка с "abc"--> (0, 3) и др параметры
print(match_object)

pattern = r"abc"
string = "babcd"
match_object = re.search(pattern, string) # проверяет имеет ли наша строка  "abc" --> (1, 4)  и др параметры
print(match_object)

pattern = r"a[abc]c" # вторым символом подходящим под шаблон может быть a, b or c (acc - подойдет)
string = "abc, acc, aac"
all_inclusions = re.findall(pattern, string) # выводит все подходящие шаблоны
print(all_inclusions)

fixed_typos = re.sub(pattern, "abc", string) # заменяет всё на "abc"
print(fixed_typos)

# pattern = r"a[a-c]c" # [a-zA-Z] -- for all simbols alphabet
# pattern = r"a.c" # for any simbols
# pattern = r"ab*a" # любое количество символа b включая 0 (aa, abba - подойдет )
# pattern = r"ab+a" # любое количество символа b от 1 
# pattern = r"ab?a" #  количество символа b от 0 до 1
# pattern = r"ab{3}a" # количество символа b 3
# pattern = r"ab{2, 4}a" # количество символа b от 2 до 4
# pattern = r"a[ab]+a" # ищит жадным способом (из abaaba - вылезит вся строка)  https://stepik.org/lesson/24470/step/4?unit=6776
# pattern = r"a[ab]+?a" # ищит наименее жадным способом (из abaaba - вылезит  aba)
# [^a-c] -- указываем что  подходит всё кроме этого
# [] - можно указывать множества подходящих символов
# . ^ $ * + ? {} [] \ | () - метасимволы
# \d ~[0-9]
# \D ~[^0-9]
# \s ~[\t\n\r\f\v]
# \S ~[^\t\n\r\f\v]
# \w ~[a-zA-Z0-9_]
# \W ~[^a-zA-Z0-9_]
# \b ~начало и конец строки включая символы короме подчеркивания # \bcat\b - находит cat во всех местах кроме обрамленных [a-zA-Z0-9_] 
# \B ~\Bcat\B - находит cat во всех местах обрамленных [a-zA-Z0-9_]
# \A ~начало строки



pattern = r" english\?" #перед знаками нужно ставить "\" иначе в pattern попадет " english" (без "?")
string = "Do you speak english?"
match = re.search(pattetn, string)
print(match)


pattern = r"(test|text)*"
string = "testtext"
match = re.match(pattern, string)
print(match) --> (0, 8)

pattern = r"abc|(test|text)*"
string = "abctest"
match = re.match(pattern, string)
print(match) --> span = (0, 3) , match = "abc" # span - координаты подходящего выражения, match - часть подошедшего выражения, берется первое подходящее


pattern = r"((abc)|(test|text)*)"
string = "testtext"
match = re.match(pattern, string)
print(match) --> span=(0, 8), match='testtext'
print(match.groups()) --> ('testtext', None, 'text')  #сперва показана группа в скобках (abc|(test|text)*, потом abc, затем test|text (показан text т.к. это последнее вхождение)
print(match.group(0)) -->testtext # по умолчанию так же 0 (print(match.group()))
print(match.group(1)) -->testtext
print(match.group(2)) -->None
print(match.group(3)) -->text


pattern = r"(\w+)-\1" # берет все символы до дефиса и сравнивает их с первой группой(тоесть с группой до дефиса, тоесть test)
string = "test-test" # если вторая часть не совпадает test-text --> None
match = re.match(pattern, string)
print(match) --> span=(0, 9), match = 'test-test'


pattern = r"(\w+)-\1" 
string = "test-test chow-chow"
duplicates = re.sub(pattern, r"\1", string) 
print(duplicates) --> test chow


pattern = r"(\w+)-\1" 
string = "test-test chow-chow"
duplicates = re.findall(pattern, string) # берет только первое слово из подошедших групп
print(duplicates) --> ['test', 'chow']


pattern = r"((\w+)-\2)"  # https://stepik.org/lesson/24470/step/5?unit=6776
string = "test-test chow-chow"
duplicates = re.findall(pattern, string)
print(duplicates) --> [('test-test', 'test'),('chow-chow', 'chow')]


x = re.match(r"text", "TEXT", re.IGNORECASE)
print(x)-->'TEXT' # и др параметры

x = re.match(r"(te)*xt", "TEXT", re.IGNORECASE | re.DEBUG)
print(x) # выводит параметры поиска


# IMPORT CSV

#first name, last name, module1, module2, module3
#students, best, 100, 100, 100
#students, good, 90, 90.2, 100  # for using ','  students, good, 90, "90,2", 100 # можно оборачивать несколько строк в кавычки (запишется вместе со '\n')
import csv

with open("example.csv") as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)

#first name last name   module1 module2 module3
#students   best    100 100 100
#students   good    90  90,2    100  

with open("example.tsv") as f: #tsv format using \t instead (вместо) "," comma
    reader = csv.reader(f, delimiter="\t")
    for row in reader:
        print(row)


students = [
    ["Greg", "Dean", 70, 80, 90, "Good job, Greg"]
    ["Wirt", "Wood", 80, 80.2, 80, "Nicely done"]
]
with open("example.csv", "a") as f:
    writer = csv.writer(f) #writer = csv.writer(f, quoting=csv.QUOTE_ALL) #поместить всё внутри кавычек
    for student in students:
        writer.writerow(student)
    #same as
    writer.writerows(students)

#IMPORT JSON
# example json
[
    {
        "first name": "Greg",
        "last name": "Dean",
        "certificate": true,
        "scores": [
            70,
            80,
            90
        ],
        "description": "Good job, Greg"
    },
    {
        "first name": "Wirt",
        "last name": "Wood",
        "certificate": true,
        "scores": [
            70,
            80,
            90
        ],
        "description": "Nicely Done"
    }
] 

import json

student1 = {
    'first name': 'Greg',
    'last name': 'Dean',
    'score': [70, 80, 90],
    'description': "Good job, Greg",
    'certificate': True
}

student2 = {
    'first name': 'Wirt',
    'last name': 'Wood',
    'score': [80, 80.2, 80],
    'description': "Nicely done",
    'certificate': True
}

data = [student1, student2]
print(json.dumps(data, indent=4, sort_keys=True)) #dumps - команда для print не путать с dump для файла, indent - количество пробелов, 
# sort_keys - сортировка ключенй в каждом объекте словаря

# for writing in file
with open("students.json", "w") as f:
    json.dump(data, f, indent=4, sort_keys=True)


#json.loads - for working in json format as python format
data = [student1, student2]
data_json = json.dumps(data, indent=4, sort_keys=True)
data_again = json.loads(data_json)
print(sum(data_again[0]["scores"])) -->240

#json.load - for working in json format as python format in file
with open("students.json", "r") as f:
    data_again = json.load(f)
    print(sum(data_again[1]["scores"])) -->240.2

# IMPORT XML

<studentsList>
    <student id='1'>
        <firstName>Greg</firstName>
        <lastName>Dean</lastName>
        <certificate>True</certificate>
        <scores>
            <module1>70</module1>
            <module2>80</module2>
            <module3>90</module3>
        </scores>
    </student>
    <student id='2'>
        <firstName>Wirt</firstName>
        <lastName>Wood</lastName>
        <certificate>True</certificate>
        <scores>
            <module1>80</module1>
            <module2>80.2</module2>
            <module3>80</module3>
        </scores>
    </student>
</studentsList>

from xml.etree import ElementTree

tree = ElementTree.parse("example.xml")
root = tree.getroot()
# root = ElementTree.fromstring(input()) - принимать из строки
print(root) # show root(main tag)
print(root.tag, root.attrib) #attrib - show attribute selected tag's

for child in root: 
    print(child.tag, child.attrib) # show tag and atribute children

print(root[0][0].text) # show children of children

for element in root.iter("scores"): # проход по заданным тегам, передав его в итер
    print(element)

for element in root.iter("scores"):
    score_sum = 0
    for child in element:
        score_sum += float(child.text)
        print(score_sum)

# writing on xml format
from xml.etree import ElementTree

tree = ElementTree.parse("example.xml")
root = tree.getroot()

tree.write("example_copy.xml") # make copy file

greg = root[0]
module = next(greg.iter("module"))
print(module1.text)
module.text = str(float(module.text) + 30) # change value on + 30

tree.write("example_modified.xml")

certificate = greg[2]
certificate.set("typy", "with distinction") #  <certificate typy="with distintion">True</certificate>

tree.write("example_modified.xml")

description = ElementTree.Element("description") # create element
description.text = "Showed excellent skills during the course"
greg.append(description)

tree.write("example_modified.xml")

description = greg.find("description") # find element inside greg
greg.remove(description) # remove element
tree.write("example_modified.xml")

#создание xml c нуля

from xml.etree import ElementTree

root = ElementTree.Element("student")
first_name = ElementTree.SubElement(root, "firstName")
first_name.text = "Greg"
second_name = ElementTree.SubElement(root, "secondName")
second_name.text = "Dean"
scores = ElementTree.SubElement(root, "scores")

module1 = ElementTree.SubElement(scores, "module1")
module.text = "100"

tree = ElementTree.ElementTree(root)
tree.write("student.xml")

# IMPORT LXML

from lxml import etree
import requests

res = requests.get("https://docs.python.org/3/")
print(res.status_code)
print(res.headers["Content-Type"])

parset = etree.HTMLParser() # работает с плохо сформированными частями язака HTML
root = etree.fromstring(res.text, parset)

for element in root.iter("a"):
    print(element, element.attrib)