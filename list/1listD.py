# # list create
# list = ['this', 'is', 'list', 'demo', '!']
# for item in dir(list):
#    print(item + '\n')
# # list read
# print(list[0]) # list[index]
# # list update
# list[0]='This'
# print(list)
# # list sort
# list.sort()
# print(list)
# # list enumrate
# e = enumerate(list)
# for i in e:
#    print(i)
# # list max
# for i in list:
#    print(i)
# # list min
# print(min(list))
# # list reverse
# list.reverse
# print(list)
# # list merge
# list2=['Merge', 'done']
# list=list+list2
# print(list)
# # list remove
# list.remove('!')
# # list concatenation
# # list repetition
# print(list[1]*3)
# # list length
# print(len(list))
# # list iteration
# # python build in function
# # python method
# # list.cmp
# list3=['this','is']
# print(cmp(list, list3))
# # list.max
# print(max(list))
# # list(seq)
# list.insert(0,'Starting...')
# print(list)
# list4=['Last...']
# list.extend(list4)
# print(list)
# list.append('End')
# print(list.count('End'))
# print(list)
# print(list[0])
# del list[0]
# print(list[0])
# listx = []
# if listx:
#    print('list is not empty')
# else:
#    print('list is empty')

import string

list_a = ['english', 'franch', 'germany']


def upper(t):
   return 'a' + t


tmp = list(map(upper, list_a))
print(tmp)



