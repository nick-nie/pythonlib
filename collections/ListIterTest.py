from collections.ListIter import ListIter

a = ListIter([1,2,3,4])
print(a.__iter__())
print(next(a))
print([i for i in a])
print([i for i in a])
