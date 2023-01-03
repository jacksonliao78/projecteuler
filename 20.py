
import math

def factorial_digits(num):
    num = math.factorial(num)
    tot = 0
    for digit in str(num):
        tot += int(digit)
    return tot

print(factorial_digits(100))