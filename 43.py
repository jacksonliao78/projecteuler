
import itertools

digits = '0123456789'
pandigits = list(''.join(num) for num in (itertools.permutations(digits, 10)))

def subdivis(num: str) -> bool:
    if int(num[1:4]) % 2 == 0:
        if int(num[2:5]) % 3 == 0:
            if int(num[3:6]) % 5 == 0:
                if int(num[4:7]) % 7 == 0:
                    if int(num[5:8]) % 11 == 0:
                        if int(num[6:9]) % 13 == 0:
                            if int(num[7:]) % 17 == 0:
                                return True
    return False


def solve():
    tot = 0
    for num in pandigits:
        if pandigits[0] != '0':
            if subdivis(num) == True:
                tot += int(num)
    print(tot)

solve()