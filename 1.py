def work(num):
    sum = 0
    for n in range(0, num):
        if n % 3 == 0 or n % 5 == 0:
            sum = sum + n

    print(sum)
    

if __name__ == "__main__":
    work(1000)
