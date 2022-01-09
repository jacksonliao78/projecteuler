
lowests = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
tens = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]

def conversion(n):
    if n < 20:
        return lowests[n]
    elif 20 <= n < 91 and n % 10 == 0:
        return tens[n / 10]
    elif 20 < n < 100:
        return tens[n // 10] + lowests[n % 10]
    elif 100 <= n < 1000 and n % 100 == 0:
        return lowests[n / 100] + "hundred"
    elif 100 < n < 1000:
        return lowests[n // 100] + "hundredand" + conversion(n % 100)
    elif n == 1000:
        return "onethousand"
    
count = 0 

for i in range(1, 1001):
    count += len(conversion(i))
print(count)





