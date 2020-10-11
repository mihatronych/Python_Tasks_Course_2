
# Итераторы
lst = [i for i in range(1, 7)]
book = {
    "title": "The Langoliers",
    "author": "Stephen King",
    'year_published': 1990
}
string = "Hello, World!"

for i in book:
    print(i)
for i in string:
    print(i)
for i in lst:
    print(i)

iterator = iter(book) # так можно посмотреть работу итератора
print(next(iterator))
print(next(iterator))
print(next(iterator))
# print(next(iterator)) # здесь будет ошибка StopIteration

while True:  # Так на самом деле работает for
    try:
        i = next(iterator)
        print(i)
    except StopIteration:
        break
# Свой маленький итератор Random

from random import random

class RandomIterator:

    def __iter__(self):
        return self

    def __init__(self, k):
        self.k = k
        self.i = 0

    def __next__(self):
        if self.i < self.k:
            self.i += 1
            return random()
        else:
            raise StopIteration

x = RandomIterator(3)
print(next(x))  # next(x) - x.__next__() x -- iterator
print(next(x))
print(next(x))

for x in RandomIterator(10):
    print(x)

# Генераторы,  помощью них реализуется отложеннное исполнение
def random_generator(k):
    for i in range(k):
        yield random()
    return "No more elements"

gen = random_generator(3)
print(type(gen))
for i in gen:
    print(i)

# Итератор пар, он кстати сломается на нечетном кол-ве элементов
class DoubleElementListIterator:
    def __init__(self, lst):
        self.lst = lst
        self.i = 0

    def __next__(self):
        if self.i < len(self.lst):
            self.i += 2
            return self.lst(self.i - 2), self.lst(self.i - 1)
        else:
            raise StopIteration


#class MyList(list):
#    def __iter__(self):
#        return DoubleElementListIterator(self)

#for pair in MyList([1, 2, 3, 4]):
#    print(pair)

# Генерация списков listcomprehantions

x = [-2, -1, 0, 1, 2]
y = [i * i for i in x if i > 0]

print(y)

z = [(x, y) for x in range(3) for y in range(3) if y >= x]
print(z)
