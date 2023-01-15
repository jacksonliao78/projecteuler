
def samedigits(num):
    if str(num)[0] != '1':
        return False
    digits = []
    for digit in str(num):
        digits.append(digit)
    for i in range(2, 7):
        num2 = num * i
        for digit in str(num2):
            if digit not in digits:
                return False
    return True
    

def solve():
    i = 0
    while True:
        i += 1
        if samedigits(i) == True:
            print(i)
            break
        
solve() # -> 142857