class Cat:
    def voice(*args):
        print('mao', args)
bob = Cat()
bob.voice()
print(Cat.voice)