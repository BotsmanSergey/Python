'''Создайте класс Vector, который хранит в себе вектор целых чисел.  У класса Vector есть:

конструктор __init__, принимающий произвольное количество аргументов. Среди всех переданных аргументов необходимо оставить только целые числа и сохранить их в атрибут values в виде списка;
переопределить метод __str__ так, чтобы экземпляр класса Vector выводился следующим образом: 
"Вектор(<value1>, <value2>, <value3>, ...)", если вектор не пустой. При этом значения должны быть упорядочены по возрастанию (будьте аккуратнее с пробелами, они стоят только после запятых, см. пример ниже);
"Пустой вектор", если наш вектор не хранит в себе значения
 

v1 = Vector(1,2,3)
print(v1) # печатает "Вектор(1, 2, 3)"
v2 = Vector()
print(v2) # печатает "Пустой вектор"'''
class Vector:
    def __init__(self, *args):
        self.values = []
        for i in args:
            if isinstance(i, int):
                self.values.append(i)
        self.values.sort()
    def __str__(self):
        if self.values:
            self.b = 'Вектор('
            self.b += str(self.values[0])
            for i in range(1, len(self.values)):
                self.b = self.b + ', ' + str(self.values[i])
            self.b+= ')'
            return self.b
        else: return 'Пустой вектор'
v1 = Vector(4,2,3)
print(v1) # печатает "Вектор(1, 2, 3)"
v2 = Vector()
print(v2) # печатает "Пустой вектор"
v3 = Vector(1)
print(v3)

# class Vector:
#     def __init__(self, *args):
#         self.values = [i for i in args if isinstance(i, int)]
#     def __str__(self):
#         return f"Вектор{tuple(sorted(self.values))}" if self.values else 'Пустой вектор'