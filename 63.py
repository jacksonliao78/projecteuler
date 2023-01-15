
from math import log10

def nth(num):
    a = len(str(num))
    return round(int(num) ** (1 / a)) ** a == num


s = 0
for n in range(1, 10):
    s += int(1 / (1 - log10(n)))
print(s)