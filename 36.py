
def pali(num):
    if str(num) == str(num)[::-1]: return True
    return False


def binary(num):
    b2 = ''
    while num > 0:
            b2 += str(num % 2)
            num = num // 2
    if pali(b2) == True:
        return True
    return False


def solve():
    tot = 0
    for i in range(1, 1000000):
        if pali(i) == True:
            if binary(i) == True:
                tot += i
    print(tot)

solve() # -> 872187
