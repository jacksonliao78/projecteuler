
def solve():
    count, p, q = 0, 1, 1
    for i in range(1000):
        num = p + 2 * q
        den = p + q
        if len(str(num)) > len(str(den)):
            count += 1
        p = num
        q = den
    print(count)


#(p + 2q)/(p + q)
solve()