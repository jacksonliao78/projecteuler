
def pentagonal(num):
    if (1 + ((1 + 24 * num) ** 0.5)) % 6 == 0: 
        return True
    return False

def solve():
    i, count = 0, 0
    while count != 3:
        i += 1
        j = i * (2 * i - 1)
        if pentagonal(j) == True:
            count += 1
    print(j)

solve() # -> 40755