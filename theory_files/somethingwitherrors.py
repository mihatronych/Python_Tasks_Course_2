# Ошибки: синтаксические (единственные узнаваемые до исполнения), исключения

# пример использования местного try catch

try:
    x = [1, 2, "hello", 7]
    x. sort()
    print(x)
except TypeError:
    print("Type error :<")

print("I can catch")


# снизу представлены разные способы использования try except
def f(x ,y):
    try:
        result =  x / y
    #except TypeError:  # isnstance?
    #    print("TypeError")
    #except (TypeError, ZeroDivisionError) as e: # isnstance?
        #print(type(e))
        #print(e)
        #print(e.args)
    #except:  # Универсально
    #    print("Маслину поймал")
    except ZeroDivisionError as e:  # все варианты обработки ошибок
        print("Маслину поймал")
        print(str(type(e)).split("\'")[1])
    else:
        print("result is", result)
    finally:
        print("finally")


#f(5, [])
try:
    print(f(5, 0))
except ArithmeticError:
    print("Arithmetic error? :<")

print(ZeroDivisionError.mro())

f(2, 1)
f(2, 0)

# Свой класс для эксэпшна
class BadName(Exception):
    pass

# Бросание исключений с помощью raise
def greet(name):
    if name[0].isupper():
        return "Hello, " + name
    else:
        raise  BadName(name + " is inappropriate name")

print(greet("Anton"))
print(greet("anton"))

while True:
    try:
        name = input("Please enter your name")
        greeting = greet(name)
        print(greeting)
    except ValueError:
        print("Plrase try again")
    else:
        break
# raise-ить можно только объекты наследующие baseexception

