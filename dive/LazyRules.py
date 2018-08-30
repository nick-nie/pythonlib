import re


class LazyRules:
    default_file = 'plural3.txt'

    def __init__(self):
        self.patter_file = open(self.default_file, encoding='utf-8')
        self.cache = []

    def __iter__(self):
        self.cache_index = 0
        return self

    def __next__(self):
        self.cache_index += 1
        if len(self.cache) >= self.cache_index:
            return self.cache[self.cache_index - 1]

        if self.patter_file.closed:
            raise StopIteration

        line = self.patter_file.readline()
        if not line:
            self.patter_file.close()
            raise StopIteration

        pattern, search, replace = line.split(None, 3)
        funcs = build_matches_and_applies_rules(pattern, search, replace)
        self.cache.append(funcs)
        return funcs


def build_matches_and_applies_rules(pattern, search, replace):
    def match_rule(word):
        return re.search(pattern, word)

    def apply_rule(word):
        return re.sub(search, replace, word)

    return match_rule, apply_rule


rules = LazyRules()


def plural3(noun):
    for match_rule, apply_rule in rules:
        if match_rule(noun):
            return apply_rule(noun)


print(rules.default_file)

print(plural3('aix'))
print(plural3('catch'))
print(plural3('apply'))
print(plural3('cat'))
