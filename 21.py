
def sum_of_div(num):
    tot = 0
    for i in range(1, num // 2 + 1):
        if num % i == 0:
            tot += i
    return tot

#finds # of amicable below num
def amicables(num):
    tot = 0
    for i in range(1, num):
        if sum_of_div((sum_of_div(i))) == i and sum_of_div(i) != i:
            tot += i
    return tot

print(amicables(10000)) # -> 31626