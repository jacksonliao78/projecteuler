
num = 149203912219012912293090
a = 0
b = 12
pos = []
def prod(n):
    if len(str(n)) == 1:
        return n
    return(n % 10 * prod(n / 10))
for i in range(1, 1000):
    x = str(num)
    y = x[a:b]
    pos.append(prod(int(y)))
    a += 1
    b += 1
print(max(pos))
    


    

   




