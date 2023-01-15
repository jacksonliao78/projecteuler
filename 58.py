
def isprime(num):
    i = 2
    while i * i <= num:
        if num % i == 0:
            return False
        i += 1
    return True

def solve():
    start, increment, primes, tot, sidelength = 1, 2, 0, 1, 1
    while True:
        for i in range(4):
            start += increment
            if isprime(start) == True:
                primes += 1
            tot += 1
        sidelength += 2
        if primes / tot < 0.1:
            print(sidelength)
            break
        else:
            increment += 2

solve() # -> 26241
