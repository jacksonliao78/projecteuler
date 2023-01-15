
def digitsum(num):
    count = 0
    for digit in str(num):
        count += int(digit)
    return count

def solve():
    biggest = 0
    for i in range(1, 101):
        for j in range(1, 101):
            if digitsum(i ** j) > biggest:
                biggest = digitsum(i ** j)
    print(biggest)

solve() # -> 972
