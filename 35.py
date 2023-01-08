

primes = [True] * 1000001
p = 2
while p * p <= 1000001:
    if primes[p] == True:
        for i in range(p * p, 1000001, p):
            primes[i] = False
    p += 1

def circular(num):
    for i in range(len(str(num))):
        if primes[num] == False:
            return False
        num = int(str(num % 10) + str(num // 10))
    return True
        

def checkdigits(num):
    bad = ['2', '4', '5', '6', '8', '0']
    for digit in str(num):
        if digit in bad:
            return False
    return True

    

def solve():
    prime = []
    for i in range(10, 1000001, 1):
        if checkdigits(i) == True:
            if circular(i) == True:
                prime.append(i)
    print(len(prime) + 4)
        
solve() # -> 55
