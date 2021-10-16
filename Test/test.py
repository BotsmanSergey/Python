def adder(value):
    def inner(a):
        return (value + a)
    return inner
a2 = adder(2)
print(a2(5))
a2(10)
a5 = adder(5)
a5(10)