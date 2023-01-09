
def pentagonal(num):
    if (1 + ((1 + 24 * num) ** 0.5)) % 6 == 0: 
        return True
    return False

def solve():
    i = 0
    while True:
        i += 1
        j = i * (3 * i - 1) / 2
        for l in range(1, i):
            k = l * (3 * l - 1) / 2
            if pentagonal(j + k) == True and pentagonal(j - k) == True:
                print(j - k)
                break
        else:
            continue
        break

solve()
            

        