# + - * / % // 

a = 21
b = 10
c = 0
print '-' * 20
print 'a = ', a
print 'b = ', b
print 'c = ', c
c = a + b
print 'Line 1 - a + b = ', c
c = a - b
print 'Line 2 - a - b = ', c
c = a * b
print 'Line 3 - a * b = ', c
c = a / b
print 'Line 4 - a / b = ', c
c = a % b
print 'Line 5 - a % b = ', c
a = 2
b = 3
c = a**b
print '-' * 20
print 'a = ', a
print 'b = ', b
print 'Line 6 - a**b = ', c
a = 10
b = 5
c = a//b
print '-' * 20
print 'a = ', a
print 'b = ', b
print 'Line 7 - a//b = ', c

# == != <> < > <= >=
print '>' * 20
a = 21
b = 10
c = 0

print 'a = ', a
print 'b = ', b

if (a == b):
    print 'Line 8 - a is equal to b'
else:
    print 'Line 8 - a is not equal to b'

if (a != b):
    print 'Line 9 - a is not equal to b'
else:
    print 'Line 9 - a is equal to b'

if (a <> b):
    print 'Line 10 - a is not equal to b'
else:
    print 'Line 10 - a is equal to b'

if (a < b):
    print 'Line 11 - a is less than b'
else:
    print 'Line 11 - a is not less than b'

if (a > b):
    print 'Line 12 - a is greater than b'
else:
    print 'Line 12 - a is not greater than b'

if (a <= b):
    print 'Line 13 - a is less than or equal to b'
else:
    print 'Line 13 - a is neither less than nor equal to b'

if (a >= b):
    print 'Line 14 - a is greater than or equal to b'
else:
    print 'Line 14 - a is neither greater than or equal to b'

# += -= *= /= %= **= //=

print '>' * 20
c = a + b
print 'Line 15 - a + b = ', c
c += a
print 'Line 16 - c += a ;c = ', c
c *= a
print 'Line 17 - c *= a ;c = ', c
c /= a
print 'Line 18 - c /= a ;c = ', c
c = 2
c %= a
print 'Line 19 - c %= a ;c = ', c
c **= a
print 'Line 20 - c **= a ;c = ', c
c //= a
print 'Line 21 - c //= a ;c = ', c


# in  not in

print '>' * 20
a = 10
b = 20
list = [1,2,3,4]

print 'a = ', a
print 'b = ', b
print 'list = ', list
if (a in list):
    print 'Line 22 - a is available in the given list'
else:
    print 'Line 22 - a is not available in the given list'

if (b not in list):
    print 'Line 23 - b is not available in the given list'
else:
    print 'Line 23 - b is available in the given list'

b = 2
print 'b = ', b
if (b in list):
    print 'Line 24 - b is available in the given list'
else:
    print 'Line 24 - b is not available in the given list'

print '>' * 20
# is  is not
a = 20
b = 20
print 'a = ', a
print 'b = ', b
if (a is b):
    print 'a and b have same idenity'
else:
    print 'a and b have diff idenity'

if (id(a) == id(b)):
    print 'a and b have same idenity'
else:
    print 'a and b have diff idenity'

if (a is not b):
    print 'a and b have diff idenity'
else:
    print 'a and b have same idenity'
