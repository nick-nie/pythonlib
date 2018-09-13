from collections import deque
import itertools

# 1.现在有一个包含 N 个元素的元组或者是序列，怎样将它里面的值解压后同时赋值给 N 个变量？
from typing import TextIO

list_a = ['f', 'g', 'h', 'i', 'j']
list_b = [40, 30, 50, 46, 39, 44]

# 2. *args
# 3. 保留最后 N 个元素

deque_a = deque(list_a, 2)
print(deque_a)


def tail(filename, n):
    """return the last n lines of a file"""
    with open(filename) as f:
        return deque(f, n)


def moving_average(iterable, n=3):
    # moving_average([40, 30, 50, 46, 39, 44]) --> 40.0 42.0 45.0 43.0
    # http://en.wikipedia.org/wiki/Moving_average
    it = iter(iterable)
    d = deque(itertools.islice(it, n-1))
    d.appendleft(0)
    s = sum(d)
    for elem in it:
        s += elem - d.popleft()
        d.append(elem)
        yield s / n


print(tail('../dive/plural3.txt', 1))
for i in moving_average(list_b):
    print(i)

