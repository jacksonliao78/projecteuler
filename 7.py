
import math
def check(n):
    if n >= 1:
        for i in range(2, n/2):
            if n % i == 0:
                return False
        return True
count = 0
n = 0
while count < 10001:
    if check(n) == True:
        count += 1
        n += 1
    n += 1
print((count), (n - 2))

    
    

             