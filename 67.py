
triangle = open('triangle.txt').read().split('\n')
triangle = [[int(num) for num in row.split()] for row in triangle]

def solve(triangle):
    for i in range(len(triangle) - 1, -1, -1):
        for j in range(0, len(triangle[i]) - 1):
            triangle[i - 1][j] = max((triangle[i][j] + triangle[i - 1][j]), (triangle[i][j + 1] + triangle[i - 1][j]))
    
    print(triangle[0][0])

solve(triangle)