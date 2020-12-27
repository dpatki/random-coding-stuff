import numpy as np
import math
grid1 = [[5,3,0,0,7,0,0,0,0],[6,0,0,1,9,5,0,0,0],[0,9,8,0,0,0,0,6,0],[8,0,0,0,6,0,0,0,3],[4,0,0,8,0,3,0,0,1],[7,0,0,0,2,0,0,0,6],[0,6,0,0,0,0,2,8,0],[0,0,0,4,1,9,0,0,5],[0,0,0,0,8,0,0,7,9]]
print(np.matrix(grid1))
def isPossible(y, x, n, grid):
    #global grid
    for i in range(0, 9):
        if grid[y][i] == n:
            return False
    for i in range(0, 9):
        if grid[i][x] == n:
            return False
    #check squares
    alpha = math.floor((y/3))*3
    beta = math.floor((x/3))*3
    for i in range(0,3):
        for j in range(0,3):
            if grid[alpha+i][beta+j] == n:
                return False
    #print("sup")
    return True


def solve(grid):
    #global grid
    for y in range(9):
        for x in range(9):
            if grid[y][x] == 0:
                for n in range(1,10):
                    if isPossible(y,x,n, grid):
                        grid[y][x] = n
                        solve(grid)
                        grid[y][x] = 0
                return
    print("hi")
    print(np.matrix(grid))
    input("hello")
#print(isPossible(4,4, 4))
solve(grid1)