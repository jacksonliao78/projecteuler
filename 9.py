
def check(a, b, c):
    if a * a + b * b == c * c:
        return True
    else:
        return False
tot = 1000
for a in range(1, 1000):
    for b in range(a + 1, 1000):
        #because we know a + b + c = 1000
        c = tot - a - b 
        if check(a, b, c) == True:
            print(a * b * c)
            break
        
        

        
