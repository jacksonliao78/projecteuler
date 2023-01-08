
primes = [True] * 1000001
p = 2
while p * p <= 1000001:
    if primes[p] == True:
        for i in range(p * p, 1000001, p):
            primes[i] = False
    p += 1
primes[1] = False

def truncate(num):
    a = num
    while num:
        if primes[num] == False:
            return False
        num = num // 10
        
    while a:
        if primes[a] == False:
            return False
        if len(str(a)) == 1:
            return True
        a = int(str(a)[1:])
    

def solve():
    tot = 0
    for i in range(10, 1000001):
        if primes[i] == True:
            if truncate(i) == True:
                tot += i
    print(tot)

solve()