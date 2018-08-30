import re


def build_matches_and_applies_rules(pattern, search, replace):
    def match_rule(word):
        return re.search(pattern, word)

    def apply_rule(word):
        return re.sub(search, replace, word)

    return (match_rule, apply_rule)


def rules(file_name):
    with open(file_name, encoding='utf-8') as pattern_file:
        for line in pattern_file:
            pattern, search, replace = line.split(None, 3)
            yield build_matches_and_applies_rules(pattern, search, replace)


def plural3(noun, rule_define_file='plural3.txt'):
    for match_rule, apply_rule in rules(rule_define_file):
        # print(rules)
        if match_rule(noun):
            return apply_rule(noun)
    raise ValueError('no matching rule for {0}'.format(noun))


print(plural3('aix'))
print(plural3('catch'))
print(plural3('apply'))
print(plural3('cat'))
