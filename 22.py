
import string

with open('names.txt') as f:
    thing = f.read().split(',')
    thing.sort()

def score(word):
    word = word.strip('"')
    return sum(string.ascii_uppercase.index(char) + 1 for char in word)

def solve(names):
    pos, tot = 1, 0
    for name in names:
        tot += score(name) * pos
        pos += 1
    print(tot)

solve(thing)