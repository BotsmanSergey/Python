'''1.На языке Python или С/С++, написать алгоритм (функцию) определения четности целого числа, который будет аналогичен нижеприведенному по функциональности, но отличен по своей сути.
Объяснить плюсы и минусы обеих реализаций.
Python example:
def isEven(value):return value%2==0
C/C++ example:
bool isEven(int value){return value%2==0;}
2. На языках Python(2.7) и/или С++, написать минимум по 2 класса реализовывающих циклический буфер. 
Объяснить плюсы и минусы каждой реализации.
3. На языке Python или С/С++, написать функцию, которая быстрее всего (по процессорным тикам) отсортирует данный ей массив чисел.
Массив может быть любого размера со случайным порядком чисел (в том числе и отсортированным).
Объяснить почему вы считаете, что функция соответствует заданным критериям.'''
# 1
def isEven2(a): return bool(not(a & 1))

print(isEven2(4))
print(isEven2(5))

# 2 решил пока только одним вариантом и не на версии 2.7, но думаю на 2.7 не сложне. Знаешь ли ты второй вариат решения?
a = [11, 22, 33, 44, 55, 66, 77]
import collections
d = collections.deque(maxlen=7)
d.extend(a)
d.append(88)
print(d)  # deque([11,22,33,44,55,66,77], maxlen=7)
# 2a
a = a[1:] + [88]
# 2b
a = [11, 22, 33, 44, 55, 66, 77]
a.append(88)
a.pop(0)
# 2c


class Array:
    def __init__(self, a):
        self.__lst = a
        self.__capacity = len(a)
        self.__start_queue = 0

    def __str__(self):
        if self.__start_queue == 0:
            return str(self.__lst[self.__start_queue:])[1:-1]
        return str(self.__lst[self.__start_queue:])[1:-1] + ', ' + str(self.__lst[:self.__start_queue])[1:-1]

    def append(self, number):
        self.__lst[self.__start_queue] = number
        self.__queue_next()

    def __queue_next(self):
        if self.__start_queue != self.__capacity:
            self.__start_queue += 1
        else:
            self.__start_queue = 0


c = Array(a)
print(c)
c.append(99)
print(c)

#2p1
class CircularBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.buffer = [None for _ in range(capacity)]
        self.curret_index = 0

    def add(self, item):
        removed_item = self.buffer[self.curret_index]
        self.buffer[self.curret_index] = item
        self.curret_index = (self.curret_index + 1) % self.capacity
        return removed_item

    def get(self, index):
        """
        Get the item at index (where 0 is the most recent item)
        """
        if index < 0 or index >= self.capacity:
            raise ValueError("Invalid index")
        return self.buffer[(self.curret_index - index - 1) % self.capacity]


if __name__ == "__main__":
    buf = CircularBuffer(4)
    buf.add(1)
    print(buf.get(0))
    buf.add(2)
    print(buf.get(1))
    buf.add(3)
    buf.add(4)
    print(buf.buffer)
    buf.add(5)
    print(buf.get(3))
    print(buf.buffer)

#2p2

class CircularBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.buffer = []

    def add(self, item):
        removed_item = None
        if len(self.buffer) == self.capacity:
            removed_item = self.buffer.pop(0)
        self.buffer.append(item)
        return removed_item

    def get(self, index):
        """
        Get the item at index (where 0 is the most recent item)
        """
        if index < 0 or index >= len(self.buffer):
            raise ValueError("Invalid index")
        return self.buffer[-index - 1]


if __name__ == "__main__":
    buf = CircularBuffer(4)
    buf.add(1)
    print(buf.get(0))
    buf.add(2)
    print(buf.get(1))
    buf.add(3)
    buf.add(4)
    print(buf.buffer)
    buf.add(5)
    print(buf.get(3))
    print(buf.buffer)

# Тут из плюсов то, что не нужно поддерживать текущий индекс, а из минусов то, что он не оптимальный и при добавлении элемента список, там создается новый массив


a = [5, 6, 2, 29, 17, 1, 3, 19, 4]
l = 0
from_l_plus_one = l + 1
j = from_l_plus_one + 1
for i in range(from_l_plus_one, j):
    if a[i] <= a[l]: 
        j += 1
        a[i], a[j] = a[j], a[i]
    print(a)