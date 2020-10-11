t_c = 18
tmp = "ok"


def fahrenheit(t_c):
    # Локальный нэймспэйс
    tmp = t_c * 9 / 5
    return tmp + 32


print(fahrenheit(t_c))
print(tmp)


# Области видимости
def b():
    x = 31

    def a():
        print(x)
    a()

b()
# Правило поиска переменных local non-local global builtins

# В циклах и условных операторах локальные пространства имен не создаются

# Поэтому то, что снизу будет работать!
for i in range(5):
    x = i * i
print(x)


# глобал и нонлокал

ok_status = True
vowels = ["a", "u", "i", "e", "o"]

def check(word):
    global ok_status # изменяй глобальную!
    for vowel in vowels:
        if vowel in word:
            return True

    ok_status = False
    return False

print(check("abacaba")) # True
print(ok_status) # True
print(check("www")) # False
print(ok_status) # False


def f():
    ok_status = True
    vowels = ["a", "u", "i", "e", "o"]

    def check(word):
        nonlocal ok_status # изменяй не локальную переменную
        for vowel in vowels:
            if vowel in word:
                return True

        ok_status = False
        return False

    print(check("abacaba")) # True
    print(ok_status) # True
    print(check("www")) # False
    print(ok_status) # False

f()
print(ok_status) # если бы я для примера глобальной переменной не писал код, то было бы Name error

