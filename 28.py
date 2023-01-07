#spiralllll
import time

def solve(num):
    start, count, tot, inc = 1, 0, 1, 2
    while count != (num - 1):
        for i in range(4):
            start += inc
            tot += start
            count += 1
        inc += 2
    print(tot)

start = time.time()
solve(2001)
end = time.time()
print(end - start)