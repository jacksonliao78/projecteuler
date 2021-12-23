
#check if prime 
def check(x):
    if x <= 1:
        return False
    for i in range(2,x):
        if x%i == 0:
            return False
    return True 

num = 600851475143 
#set to hold possible primes; include 1
pos = []
pos.append(1)
for i in range(2,num//2+1): #divide by 2, no decimal + 1
    if num%i == 0: #if number is a factor
        if check(i)== True: #if prime
            pos.append(i)

print(max(pos))

