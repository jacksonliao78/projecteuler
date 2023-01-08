
#champ er no W ne

def solve():
    i, long = 1, ''
    while len(long) < 1000000:
        long += str(i)
        i += 1
    print(int(long[0]) * int(long[9]) * int(long[99]) * int(long[999]) * int(long[9999]) * int(long[99999]) * int(long[999999]))

solve()
