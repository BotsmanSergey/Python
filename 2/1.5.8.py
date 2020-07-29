class MoneyBox:
    def __init__(self, capacity):
        self.capacity = capacity
        self.count = 0
    def can_add(self, v):
        if v <= self.capacity - self.count:
            return True
        else:
            return False
        # True, если можно добавить v монет, False иначе
    def add(self, v):
        self.count += v
        # положить v монет в копилку