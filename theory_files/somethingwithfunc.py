def func_name(argument1):
    print(argument1)
    return argument1


def list_sum(lst):
    result = 0
    for element in lst:
        result += element
    return result


def sum(a, b):
    return a + b


y = sum(14, 29)
z = list_sum([1, 2, 3])
#все эти функции создают дофига объектов, поэтому в будущем стоит не перебарщивать
print(y)
print([1, 2].append(z))


#simple_stek_work
x = [1, 2, 3]
x.append(4)
x.append(5)

print(x)

top = x.pop()
print(top)
print(x)


def printab(a, b=20):
    print(a)
    print(b)


#CORRECT WAYS TO CALL A FUNC
printab(10, 20)
printab(a=11, b=21)
printab(10)
#keyword args always after non-keyword args
printab(12, b=22)

lst = [13, 23]
printab(*lst)

args = {'a' : 14, 'b' : 24}
printab(**args)

def printab(a, b, *args):
    print("pos arg a", a)
    print("pos arg b", b)
    print("additional args:")
    for arg in args:
        print(arg)

printab(10, 20, 30, 40, 50)

def printab(a, b, **kwargs):
    print("pos arg a", a)
    print("pos arg b", b)
    print("additional args:")
    for key in kwargs:
        print(key, kwargs[key])

printab(10, b=20, c=30, d=40, jimmi=123)

#Формально верное определение функции
#def function_name(
#        [ positional_args,
#        [ positional_args_with_default,
#        [ *pos_args_name,
#        [keyword_only_args,
#        [ **kw_args_name]]]]]):

##Пример формально полной функции
def printab(a, b=10, *args, c=10, d, **kwargs):
    print(a, b, c, d)


printab(15, d=15)

def s(a, *vs, b=10):
   res = a + b
   for v in vs:
       res += v
   return res

print(s(11,10))

#Рекурсивная функция
def fib(x):
    if x == 0 or x == 1:
        return 1
    else:
        return fib(x - 1) + fib(x - 2)

y = fib(5)
print(y)