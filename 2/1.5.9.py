class Buffer:
    def __init__(self):
        self.n = []
        # конструктор без аргументов

    def add(self, *a):
        for i in a:
            self.n.append(i)
        while len(self.n) >= 5:
            sum = 0
            for i in range(5):
                sum += self.n[i]
            del self.n[:5]
            print(sum)
        # добавить следующую часть последовательности
    def get_current_part(self):
        return self.n
        # вернуть сохраненные в текущий момент элементы последовательности в порядке, в котором они были добавлены