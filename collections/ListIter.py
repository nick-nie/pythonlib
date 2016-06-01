class ListIter(object):
    def __init__(self, data):
        self.__data = data
        self.__count = 0
 
    def __iter__(self):
        return self
 
    def next(self):
        if self.__count < len(self.__data):
            val = self.__data[self.__count]
            self.__count += 1
            return val
        else:
            raise StopIteration
