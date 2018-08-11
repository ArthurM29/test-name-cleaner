import re

filename = r'tests.txt'
pattern = r'\w+.+'    # match a line without pass/fail icons

with open(filename) as f:
    for line in f.readlines():
        line_without_icons = re.search(pattern, line).group()
        sentence = re.sub(r'\(\w+\)', '', line_without_icons.rstrip())  # remove (2 ms)
        if sentence.startswith('when'):
            sentence = '\n' + sentence + '\n'
        print(sentence)
