# -*- coding: utf-8 -*-
class Fibo:
    def __init__(self, volume):
        self.max = volume

    def __iter__(self):
        self.a = 0
        self.b = 1
        return self

    def __next__(self):
        fibo = self.a
        if self.a > self.max:
            raise StopIteration
        self.a, self.b = self.b, self.a + self.b
        return fibo


# def fib(volume):
#     a, b = 0, 1  # a = 初始值， b = a + b
#     while a < volume:
#         yield a
#         a, b = b, a + b
#
#
# print(list(fib(10)))

fib = Fibo(20)
print(fib.max)
for i in fib:
    print(i)
