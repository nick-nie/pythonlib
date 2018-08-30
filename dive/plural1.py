# 在英语中，若字母以 s, x, z 结尾，则替换为 es
import re


def plural1(noun):
    if re.search('[sxz]$',noun):
        return re.sub('[sxz]$', 'es', noun)
    if re.search(r'[^aeioudgkprt]h$', noun):
        return re.sub('$', 'es', noun)
    if re.search(r'[^aeiou]y$', noun):
        return re.sub('y$', 'ies', noun)
    else:
        return noun + 's'


print(plural1('aix'))
print(plural1('catch'))
print(plural1('apply'))
print(plural1('cat'))

