
x = 100
sum = 0
sum2 = 0
sum3 = 0
for i in range(1, x + 1, +1):
    a = i * i
    sum += a
for i in range(1, x + 1, +1):
    sum2 += i
sum3 = sum2 * sum2
print(sum3 - sum)

