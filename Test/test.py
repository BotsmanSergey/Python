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
a == b  
b > a   #хоть мы и не делали __gt__, Python пробует перевернуть a < b и такая функция есть
#но нужно что бы второй аргумент тоже имел функцию a.__lt__(b).
b != a  # not (b == a) , __ne__ можно не реализовывать
b >= a  # a <= b