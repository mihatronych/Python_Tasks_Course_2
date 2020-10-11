class MoneyBox:
    def __init__(self, capacity):
        self.capacity = capacity
        # конструктор с аргументом – вместимость копилки

    def can_add(self, v):
        return v <= self.capacity
        # True, если можно добавить v монет, False иначе

    def add(self, v):
        if self.can_add(v):
            self.capacity -= v
        # положить v монет в копилку
