# Python Date and Time

import time

localtime = time.localtime(time.time())
print(('Local Time is :', localtime))

localtime1 = time.asctime(localtime)
print(('Asctime is:', localtime1))

print((time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())))

print((time.strftime('%a %b %d ', time.localtime())))
