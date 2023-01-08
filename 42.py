
import string

with open('words.txt') as f:
    words = f.read().split(",")
    words = [word.strip('"') for word in words]

def score(word: str) -> int:
    return sum(string.ascii_uppercase.index(char) + 1 for char in word)

def solve():
    count2, count, triangle = 0, 1, []
    while count != 500:
        triangle.append((count * 0.5) * (count + 1))
        count += 1
    for word in words:
        if score(word) in triangle:
            count2 += 1
    print(count2)

solve()
            


