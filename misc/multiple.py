memory=1200
size=2
for i in range(0, 10):
    memory /= size
    print(memory)


tup = (('key1','value1'),('key2','value2'),('key3','value3'))
for key, value in tup:
    print(key,value)