
def prime(n):
    mult = set()
    primes = []
    tot = 0
    for i in range(2, n):
        if i not in mult:
            for j in range(i ** 2, n, +i):
                mult.add(j)
            primes.append(i)
            tot += i
    print(tot)
    
print(prime(2000000))

