import sys

def test():
    args = sys.argv
    if len(args)==1:
        print('Hello, world!')
    elif len(args)==2:
        print('Hellow, %s' % args[1])
    else:
        print('Too many arguments!')

if __name__== '__main__':
    test()
    for e in enumerate(dir(sys)):
        print(e)

info = sys.path
for e in enumerate(info):
    print(e)

print(sys.platform)
print(sys.version)
print(sys.version_info)
print(sys.getprofile)
