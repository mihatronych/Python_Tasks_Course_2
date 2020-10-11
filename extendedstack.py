class ExtendedStack(list):
    def sum(self):
        if len(self) >= 2:
            self.append(self.pop() + self.pop())
        # операция сложения

    def sub(self):
        if len(self) >= 2:
            self.append(self.pop() - self.pop())
        # операция вычитания

    def mul(self):
        if len(self) >= 2:
            self.append(self.pop() * self.pop())
        # операция умножения

    def div(self):
        if len(self) >= 2:
            self.append(self.pop() // self.pop())
        # операция целочисленного деления