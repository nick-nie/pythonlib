book = {'name':'Python Core Programing','author':'micheal','date':'2015-12-12'}
for e in enumerate(dir(book)):
        print e

print '='*20

for k,v in book.items():
        print k, v
print '='*20

print type(book)
