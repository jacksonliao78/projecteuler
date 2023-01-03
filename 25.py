
def solve():
    fib = [0 , 1]
    i = 2
    while len(str(fib[-1])) != 1000:
        fib.append(fib[i - 1] + fib[i - 2])
        i += 1
    print(fib.index((fib[-1])))

solve() # -> 4782
        