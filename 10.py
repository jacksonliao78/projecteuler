
def prime(n):
    mult = []
    primes = []
    tot = 0
    for i in range(2, n):
        if i not in mult:
            tot += i
            primes.append(i)
            for j in range(i ** 2, n, +i):
                mult.append(j)
    print(tot)
    
print(prime(2000000))

