# while demo
i = 0
while (i < 9):
    print '*' * i
    i += 1


#
print '>' * 20
word = 'python'
print 'given word:' + word
print 'len of word:' + str(len(word))
for letter in 'python':
    print 'current letter:', letter

fruits = ['apple', 'banana', 'mango']
for fruit in fruits:
    print 'current fruit:', fruit


for index in range(len(fruits)):
    print 'current fruit:', fruits[index]


for num in range (10, 20):          # to iterate between 10 to 20
    for i in range (2, num):        # to iterate the factors of the number
        if num%i == 0:              # to determine the first factor
            j=num/i                 # to calculate the second factor
            print '%d equals %d * %d' % (num,i,j)
            break                   # to move the next number, the #first FOR
    else:                           # else part of the loop
            print num, 'is a prime number'

    
