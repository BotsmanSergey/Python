'''Создайте класс Money, у которого есть:
конструктор __init__, принимающий 2 аргумента: dollars, cents. По входным аргументам вам необходимо 
создать атрибут экземпляра total_cents. 
свойство геттер dollars, которое возвращает количество имеющихся долларов;
свойство сеттер dollars, которое принимает целое неотрицательное число - количество долларов и 
устанавливает при помощи него новое значение в атрибут экземпляра total_cents, при этом значение центов 
должно сохранятся. В случае, если в сеттер передано число, не удовлетворяющее условию, нужно печатать на 
экран сообщение "Error dollars";
свойство геттер cents, которое возвращает количество имеющихся центов;
свойство сеттер cents, которое принимает целое неотрицательное число меньшее 100 - количество центов и 
устанавливает при помощи него новое значение в атрибут экземпляра total_cents, при этом значение долларов
должно сохранятся. В случае, если в сеттер передано число, не удовлетворяющее условию, нужно печатать на
кран сообщение "Error cents";
метод __str__ (информация по данному методу), который возвращает строку вида "Ваше состояние составляет
{dollars} долларов {cents} центов". Для нахождения долларов и центов в методе __str__ пользуйтесь 
свойствами
В экземпляр класса кроме атрибута total_cents сохранять ничего не нужно!
Bill = Money(101, 99)
print(Bill)  # Ваше состояние составляет 101 долларов 99 центов
print(Bill.dollars, Bill.cents)  # 101 99
Bill.dollars = 666
print(Bill)  # Ваше состояние составляет 666 долларов 99 центов
Bill.cents = 12
print(Bill)  # Ваше состояние составляет 666 долларов 12 центов'''

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

    def __str__(self):
        return f"Ваше состояние составляет {self.total_cents//100} долларов {self.total_cents%100} центов"
Bill = Money(101, 99)
print(Bill)  # Ваше состояние составляет 101 долларов 99 центов
print(Bill.dollars, Bill.cents)  # 101 99
Bill.dollars = 666
print(Bill)  # Ваше состояние составляет 666 долларов 99 центов
Bill.cents = 12
print(Bill)  # Ваше состояние составляет 666 долларов 12 центов
Bill.dollars = 'sdf'
Bill.dollars = 1.0
Bill.cents =1.0
Bill.cents = 100    