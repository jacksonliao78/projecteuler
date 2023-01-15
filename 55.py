
def palindrome(num):
    return str(num) == str(num)[::-1]

def lychrel(num):
    count = 0
    while count != 50:
        if palindrome(num + int(str(num)[::-1])) == True:
            return False
        else:
            num = num + int(str(num)[::-1])
            count += 1
    return True

def solve():
    count = 0
    for i in range(1, 10001):
        if lychrel(i) == True:
            count += 1
    print(count)

solve() # -> 249

