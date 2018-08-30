def fib(max):
    a , b = 0, 1 # a = 初始值， b = a + b
    while a < max:
        yield a
        a, b = b, a + b


list(fib(10)) # return list

print(list(fib(10)))