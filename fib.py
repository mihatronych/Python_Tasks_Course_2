print(__name__)  # в данном коде это main, а если импорт, то превратится в fib

def fib(k):
    if k == 0 or k == 1:
        return 1
    else:
        return fib(k - 1) + fib(k - 2)

if __name__ == "__main__":
    print(fib(31))
    print(__name__)
