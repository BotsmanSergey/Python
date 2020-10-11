cd #выбор дирректории
python # запуск интерпритатора 
quit #выход из интерпритатора
python test.py # запуск файла

print("Hello", name)
int(-2.3) --> -2
floal(5) --> 5
type(7) --> int # вычесление типа
s = int(input('Введите данные')) # ждет данные от пользователя и переводит в int и сохраняет в s

x y or and not
0 0 0  0   1
0 1 1  0   1
1 0 1  0   0
1 1 1  1   0
# по порядку вычисления not and or

a = 10
print(10<=a<100)-->True
print('*', end='') # печать символа без переноса на следующюю строку

if (x=1):
    print(1)
elif (x=2)
    print(2)
else:
    print(3)

len('abcdef') --> 6
'\n' #символ перевода строк
'\t' #символ табуляции
# # комментарий

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

y = [i*i for i in x if i > 0]
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

# строки не изменяемы
genome = 'ATTG'
for c in genome:
    print(c)   # проход по строке

genome = 'ATTG'
print(genome.count('T')) # считает сколько T в genome 

s='aTGcc' p='cc'
s.upper() --> 'ATGCC'
s.lower() --> 'atgcc'
s.count(p) --> 1 # количество не пересекающихся вхождений
s.find(p) --> 3
s.rfind(p)#см выше, только проверка идет справа
s.find('A') --> -1 #  не входит
if 'TG' in s:-->True #проверка вхождения в строку
s.replace('c', 'C') --> 'aTGCC'
s.index("TG")-->1 #index of first вхождения or ValueError
s.startswith("The man in black") # проверка начинается ли строка с данного набора символов, функция может принемать кортеж
s.endswith(".png")# см. выше, только проверяет окончание строки
s.split() # разделение по пробелу или заданному символу
s.strip() # clear simbols("\t", " ")
s.rstrip()# clear right side
s.lstrip()# clear left side


s = 'agTtcAGtc'
genome.upper().count('gt'.upper()) --> 2 # с начала поднимает s, потом поиск поднятого gt


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

# СПИСКИ
students = [] # пустой список
students = ['olya', 'seriy', 'pasha'] # заполненный список
for student in students:
   print("hello, " + student + "!")

# можно явно исменять список: 
students[0] = 'Olya'
students += ['Katya'] или students.append('Katya') # students += 'Katya' прибавит 5 элементов в список
students.insets(1, 'Boris') # вставляет элемент между 0 и 1 элементами
students.remove('Boris') # удаляет первое вхождение элемента 'Boris'
del students[0] # удаляет нулевой элемент

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

a = [[0] * n for i in  range(n)]
a = [[0 for j in range(n)] for i in range(n)]

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

# NONELOCAL VARIABLE

def f():
    ok_status = True
    vowels = ["a", "u", "i", "e", "o"]
    def check(word):
        nonlocal ok_status # для использования переменных на уровень или несколько выше видимости выше
            for vowel in vowels:
                if vowerl in word:
                    return = False
            ok_status = False
            return False

f()
print(ok_status) --> NameError


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

 

os.path.join('.', 'dirname', 'filename.txt') # подключаемый модуль позволяющий переделывать путь к файлу в разных ОС --> './dirname/filename.txt'

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

# КОРТЕЖИ

# не изменяемы, быстрее чем списки, можно использовать в качестве ключей словаря
# не имеют метода index, но имеют in

info = ('a', 0, False, (4, 5, 6), [])
g = (5) # это не кортеж
info[3:4] # срезы в кортежах это новый кортеж

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
print(MyClass.a) # MyClass.a отребут класса MyClass
print(MyClass.func) #  MyClass.func отребут класса MyClass
# в отличии от функций тело класса исполняется в момент определения самого класса и за ним закрепляется определенный namespace

# OBJECT OF CLASS

class MyClass:
    a = 10
    def func(self):
        print('Hello')
x = MyClass() # x is instance(экземпляр) of class MyClass. MyClass() it's constructor of class MyClass
print(type(x))
print(type(MyClass))


class Counter:
    pass # when hollow(empty) class
Counter -->class object
x = Counter # x is instant object
x.count = 0
x.count += 1


class Counter:
    def __init__(self):  # a function __init__ принимает ещё не существующий instance(экземпляр) self
        self.count = 0 # к ещё не существующему instance, add атрибут
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

class Counter:
    def __init__(self):  
        self.count = 0
    def inc(self):
        self.count += 1
    def reset(self):
        self.count = 0
# Counter
x = Counter()
x.inc --> 1
print(x.count)
Counter.inc(x) -->2 # Тоже самое что и x.inc строчкой выше (Bound Method(связанный метод))
print(x.count)
x.reset()-->0
print(x.count)

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
print(match) --> span = (0, 3) , match = "abc"
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