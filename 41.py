
primes = [True] * 100000001
p = 2
while p * p <= 100000001:
    if primes[p] == True:
        for i in range(p * p, 100000001, p):
            primes[i] = False
    p += 1
primes[1] = False

def checkdigits(num):
    digits = [True] * len(str(num))
    for digit in str(num):
        if digit == '0' or int(digit) > len(str(num)):
            return False
        if digits[int(digit) - 1] == True:
            digits[int(digit) - 1] = False
        else: return False
    return True

def solve():
    pan = []
    for i in range(10, 100000001):
        if primes[i] == True:
            if checkdigits(i) == True:
                pan.append(i)
    print(max(pan))

solve()

