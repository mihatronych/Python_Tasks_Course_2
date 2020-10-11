# Наслшедование
# class DerivedClassName(Base1, Base2, Base3):
#    <statement-1>
#    ...
#    <statement-N>


class MyList(list):  # Этот класс наследует от класса list
    def even_length(self):
        return len(self) % 2 == 0


x = MyList()
print(x)  # []
x.extend([1, 2, 3, 4, 5])
print(x)
print(x.even_length())  # False
x.append(6)
print(x.even_length())  # True


# Множественное наследование
class D: pass


class E: pass


class B(D, E): pass


class C: pass


class A(B,
        C): pass  # В данном примере все классы кроме класса А - предки класса А, а класс А потомок всех остальных классов


issubclass(A, A)  # True
issubclass(C, D)  # False
issubclass(A, D)  # True А - наследник класса D
issubclass(C, object)  # True
issubclass(object, C)  # False

x = A()
isinstance(x, A)  # True Является ли тип первого аргумента наследником второго аргумента
isinstance(x, B)  # True
isinstance(x, object)  # True
isinstance(x, str)  # False

x = MyList()
isinstance(x, list)  # True

# Последовательность наследования при множественном наследовании


class Cat():
    def say(self, times):
        print('Meow ' * times)


class Dog():
    def say(self, times):
        print('Bow-Wow ' * times)


class CatDog(Cat, Dog):
    pass


class DogCat(Dog, Cat):
    pass


muteDog = CatDog()
muteDog.say(3)  # Meow Meow Meow
# mro - method resolution order
print(CatDog.mro())  # [<class '__main__.CatDog'>, <class '__main__.Cat'>, <class '__main__.Dog'>, <class 'object'>]

muteCat = DogCat()
muteCat.say(2)  # Bow-Wow Bow-Wow
print(DogCat.mro())  # [<class '__main__.DogCat'>, <class '__main__.Dog'>, <class '__main__.Cat'>, <class 'object'>]

class EvenLengthMixin:
    def even_length(self):
        return len(self) % 2 == 0


class MyList(list, EvenLengthMixin):
    def pop(self):
        x = super(MyList, self.pop())  # Це наследуется от list.pop(self)
        print("Last value is", x)
        return x


ml = MyList([1, 2, 4, 17])
z = ml.pop()  # Last value i 17
print(z)  # 17
print(ml)  # [1, 2, 4]
