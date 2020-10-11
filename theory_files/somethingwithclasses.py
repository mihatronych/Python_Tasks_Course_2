# Пример класса
class MyClass:
    a = 10

    def func(self):
        print("Hello")


print(MyClass.a)
print(MyClass.func)

# Пример конструктора
x = MyClass()
print(type(x))
# <class '_main_.MyClass'>
print(type(MyClass))


# <class 'type'>


class Counter:
    pass


# Атрибуты
Counter  # class object
x = Counter()  # x is instance object
x.count = 0
x.count += 1


# Класс с конструктором класса
class Counter2:
    def __init__(self):
        self.count = 0

    def __init__(self, start=0): # Конструктор с атрибутом
        self.count = start

    def inc(self): # Методы класса
        self.count += 1

    def reset(self):
        self.count = 0


Counter2  # class object
x = Counter2(5)
print(x.count)  # 0
x.count += 1
x.inc() # - Bound Method
print(x.count)
Counter2.inc(x) # Это по сути равно x.inc()  наоборот
print(x.count)
x.reset()
print(x.count)

class Song:
    # tags = [] - если бы тэги были определены так, то они менялись бы для всего класса, а не для отдельных его экземпляров

    def __init__(self, artist, song):
        self.artist = artist
        self.song = song
        self.tags = [] # вот так оно робит для экземпляра класса

    def add_tags(self, *args):
        self.tags.extend(args)

