
a = 999
palin = []
for b in range(a, 100, -1):
    for c in range(b, 100, -1):
        d = b * c        
        pos = str(d)
        if pos == pos[::-1]:
           palin.append(pos)
print(max(palin))
        
   