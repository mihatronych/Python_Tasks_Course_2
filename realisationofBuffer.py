class Buffer:
    def __init__(self):
        self.lst = []
        # конструктор без аргументов

    def add(self, *a):
        self.lst += a
        while len(self.lst) >= 5:
            print(sum(self.lst[0:5]))
            self.lst = self.lst[5:]
        # добавить следующую часть последовательности

    def get_current_part(self):
        return self.lst
        # вернуть сохраненные в текущий момент элементы последовательности в порядке, в котором они были
        # добавлены

buf = Buffer()
buf.add(1, 2, 3)
print(buf.get_current_part()) # вернуть [1, 2, 3]
buf.add(4, 5, 6) # print(15) – вывод суммы первой пятерки элементов
print(buf.get_current_part()) # вернуть [6]
buf.add(7, 8, 9, 10) # print(40) – вывод суммы второй пятерки элементов
print(buf.get_current_part()) # вернуть []
buf.add(1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1) # print(5), print(5) – вывод сумм третьей и четвертой пятерки
print(buf.get_current_part()) # вернуть [1]
