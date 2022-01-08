
chain = 1
big = 0
num = 0

for i in range(1,1000000):
    temp = i
    while i > 2:
        if i % 2 == 0:
            i = i / 2
            chain += 1
        if i % 2 == 1:
            i = (3 * i) + 1
            chain += 1
    if chain > big:
        big = chain
        num = temp
    chain = 1
    
print(num)
print(big)

        
