
import itertools

#below is a super tedious solution that I made; the code just kept running so I scrapped it

def permutation(num):
    if len(str(num)) == 9:
        digits = [False] * 9
        for digit in str(num):
            if digit != '0':
                if digits[int(digit) - 1] == False:
                    digits[int(digit) - 1] = True
                else:  
                    return False
            else:
                return False
        return True
    else:
        digits = [False] * 10
        for digit in str(num):
            if digits[int(digit)] == False:
                digits[int(digit)] = True
            else:  
                return False
        return True

def solve(num):
    count = 0
    start = 123456789
    while count != num:
        if permutation(start) == True:
            count += 1
        start += 1
    print(start - 1)

#makes use of itertools (permutations())    
#10 is length of tuple, joins the tuple and sorts the tuples

def solve2():
    digits = '0123456789' #the iterable
    thing = sorted(''.join(num) for num in (itertools.permutations(digits, 10)))
    print(thing[999999])

solve2() # -> 2783915460