
def abundant(num):
    tot = 0
    for i in range(1, num // 2 + 1):
        if num % i == 0:
            tot += i
    if tot > num:
        return True
    return False

def solve(num):
    abu = []
    for i in range(0, num):
        if abundant(i) == True:
            abu.append(i)
    tots = [0] * (num + 1)
    for i in range(0, len(abu)):
        for j in range(i, len(abu)):
            sum_of_two = abu[i] + abu[j]
            if sum_of_two <= num:
                if tots[sum_of_two] == 0:
                    tots[sum_of_two] = sum_of_two
    tot = 0
    for i in range(0, num):
        if tots[i] == 0:
            tot += i
    print(tot)

    
solve(28123)