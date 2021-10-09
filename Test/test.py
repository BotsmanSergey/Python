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
p.my_balance# скобки не нужны так как это свойства  
p.my_balance = 901
p.my_balance
del p.my_balance
p.my_balance