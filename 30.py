
def sumofdigits(num):
    tot = 0
    for digit in str(num):
        tot += (int(digit) ** 5)
    return tot


def solve():
    tot = 0
    for i in range(2, 354295):
        if sumofdigits(i) == i:
            tot += i
    print(tot)

solve() # -> 443839
