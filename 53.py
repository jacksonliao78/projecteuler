
import math

def perm(n, k):
    return math.factorial(n) / (math.factorial(k) * math.factorial(n - k))
    
def solve():
    count = 0
    for i in range(23, 101):
        for j in range(2, i + 1):
            if perm(i, j) > 1000000:
                count += 1
    print(count)

solve() # -> 4075