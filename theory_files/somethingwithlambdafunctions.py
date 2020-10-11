# лямбда функции и всякое

n, k = map(int, input().split())  # Использование map - он на самом деле итератор,
# и здесь робит мехванизм распаковки, но робит он довольно долго
n, k = (int(i) for i in input().split()) # Это будет работать быстрее
print(n + k)

x = input().split()
xs = (int(i) for i in x)

#def even(x):
#    return x % 2 == 0
even = lambda x: \
    x % 2 == 0  # можно записать лямбд-функцией сначала аргумент, а потом выражение

evens = list(filter(even, xs))  # Фильтр фильтрует по значению истинности функции элементы списка
print(evens)

evens = list(filter(lambda x: x % 2 == 0, xs))  # запись с лямбда функцией
print(evens)
# лямбду придется писать в одно выражение

x = [
    ["Guido", "van", "Rossum"],
    ["Haskell", "Curry"],
    ["John", "Backus"]
]

def length(name):
    return len(" ".join(name))

name_lengths = [length(name) for name in x]
print(name_lengths)

#x.sort(key=length)  # Ключ для сортировки по возрастанию длины
#print(x)

# А можно короче!

#x.sort(key=lambda name: len(" ".join(name)))
#print(x)

# Можно еще короче, но с использ0ованием библиотеки operator
#import operator as oper
#x.sort(key=oper.itemgetter(-1))
#print(x)

# И с functool!
import operator as oper
from functools import partial

sort_by_last = partial(list.sort, key=oper.itemgetter(-1))
print(x)
sort_by_last(x)  # Им можно сортировать по последнему аргументу, что угодно
print(x)
# Работа с библиотекой операторов
import operator as op  # библиотека различных операторов

print(op.add(4, 5))
print(op.mul(4, 5))
print(op.contains([1, 2, 3], 4))

x = [1, 2, 3]
f = op.itemgetter(1)  # f(x) == x[1]  берет item объекта
print(f(x))

f = op.attrgetter("sort")  # f(x) == x.sort !
print(f([1,3,4,6,2,0]))

# Библиотека functools
from functools import partial

x = int("1101", base=2)
print(x)
int_2 = partial(int, base=2)
x = int_2("1101")
print(x)
