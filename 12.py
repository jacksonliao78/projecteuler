

def check(n):
    divs = 0
    for i in range(1, n):
        if n % i == 0:
            divs += 1
            if divs == 501:
                return True
            continue
    return False
    
            
bruh = 0
n = 2
tot = 1

while bruh != 1:
    if check(tot) == True:
        print(tot)
        bruh = 1
    tot += n
    n += 1


    
    
    
