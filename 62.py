
import itertools

def iscube(num):
    if round(int(num) ** (1 / 3)) ** 3 == int(num):
        return True
    return False

def permutations(num):
    perms = [*set(list(''.join(num) for num in (itertools.permutations(str(num)))))]
    count = 0
    for perm in perms:
        if len(str(int(perm))) == len(str(num)):
            if iscube(perm) == True:
                count += 1
    return count

def solve():
    i = 0
    while True:
        i += 1
        if permutations(i ** 3) == 5:
            print(i ** 3)
            break
    
# ^brute force algo that takes too long

def solve2():
    i, cubes = 0, []
    while True:
        helpfulvariable = sorted(list(str(i ** 3)))
        cubes.append(helpfulvariable)
        if cubes.count(helpfulvariable) == 5:
            print(cubes.index(helpfulvariable) ** 3)
            break
        i += 1
    
solve2() # -> 127035954683
        
