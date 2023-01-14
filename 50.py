
primes = [True] * 1000001
p = 2
while p * p <= 1000001:
    if primes[p] == True:
        for i in range(p * p, 1000001, p):
            primes[i] = False
    p += 1
primes[1], primes[0] = False, False
primes2 = []
for i in range(1000001):
    if primes[i] == True:
        primes2.append(i)


def solve():
    longest = 0
    prim = 0
    last = len(primes2)

    for i in range(len(primes2)):
        for j in range(i + longest, last):
            if sum(primes2[i:j]) < 1000001:
                if sum(primes2[i:j]) in primes2:
                    longest = j - i
                    prim = sum(primes2[i:j])
            else:
                last = j + 1
                break

    print(prim)

solve()
