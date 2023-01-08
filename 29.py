
def solve():
    vals = []
    for i in range(2, 101):
        for j in range(2, 101):
            vals.append(i ** j)
    vals = list(set(vals))
    print(len(vals))

solve() # -> 9183