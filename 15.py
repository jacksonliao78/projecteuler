
import math

n = 20

#n is the length of the grid 
def paths(n):
    return math.factorial(n)
    
print(paths(2 * n) / paths(n) / paths(n))


