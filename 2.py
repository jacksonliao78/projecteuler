
num1 = 1
num2 = 1
num3 = 0
result = 0
while result <= 4000000:
        num3 = num2 + num1
        if num3%2 == 0:
                result = result + num3

        num1 = num2
        num2 = num3
print (result)
