
a = 999
n = 0
for b in range(a, 100, -1):
    for c in range(b, 100, -1):
        d = b * c
        if d > n:
            pos = str(d)
            if pos == pos[::-1]:
                print(b,c)
                break
        
   