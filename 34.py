
import math


def sumofdigits(num):
    tot = 0
    for digit in str(num):
        tot += math.factorial(int(digit))
    return tot
    

def solve():
    tot = 0
    for i in range(3, 2540161):
        if sumofdigits(i) == i:
            tot += i
    print(tot)

solve()

