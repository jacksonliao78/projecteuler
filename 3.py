
n = 600851475143 
def largest(n):
    i = 2 
    #largest prime factor can't be bigger than sqrt of n
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
    return n
          
print(largest(n))


