
import math

def check(n):
    divs = 1
    count2 = 1
    count3 = 1
    temp = n
    while n % 2 == 0:
        n = n / 2
        count2 += 1
    divs *= count2
    
    for i in range(3, temp / 2, +2):
        while n % i == 0:
            n = n / i
            count3 += 1
        divs *= count3
        count3 = 1
    return divs
        

switch = 0
n = 2
tot = 1

while switch != 1:
    if check(tot) > 200:
        print(tot)
        switch = 1
    tot += n
    n += 1
  


    
    
    
