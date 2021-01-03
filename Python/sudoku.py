import numpy as np
import math
import sys
grid1 = [[5,3,0,0,7,0,0,0,0],[6,0,0,1,9,5,0,0,0],[0,9,8,0,0,0,0,6,0],[8,0,0,0,6,0,0,0,3],[4,0,0,8,0,3,0,0,1],[7,0,0,0,2,0,0,0,6],[0,6,0,0,0,0,2,8,0],[0,0,0,4,1,9,0,0,5],[0,0,0,0,8,0,0,7,9]]
grid2 = [[".",".","4",".",".",".","6","3","."],[".",".",".",".",".",".",".",".","."],["5",".",".",".",".",".",".","9","."],[".",".",".","5","6",".",".",".","."],["4",".","3",".",".",".",".",".","1"],[".",".",".","7",".",".",".",".","."],[".",".",".","5",".",".",".",".","."],[".",".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".",".","."]]
#print(np.matrix(grid2))
def isValidSudoku(board):
    """
        :type board: List[List[str]]
        :rtype: bool
    """
    #check cols
    for x in range(9):
        tempdict = {}
        for y in range(9):   
            #print(temparr)
            #print(board[y][x])
            #print(tempdict)
            if board[y][x] in tempdict:
                if board[y][x] != 0:
                    #print("colfail at " + str(x) + str(y))
                    return False
            tempdict[board[y][x]] = 1
    #check rows
    for y in range(9):
        tempdict = {}
        for x in range(9):  
            #print(board[y][x])
            #print(tempdict) 
            if board[y][x] in tempdict:
                if board[y][x] != 0:
                    #print("rowfail at " + str(y) + str(x))
                    return False
            tempdict[board[y][x]] = 1
    #check squares
    for alpha in range(3):
        for beta in range(3):    
            tempdict = {}
            for y in range(3*alpha, 3*alpha + 3):
                for x in range(3*beta, 3*beta + 3):
                    #print(board[y][x])
                    #print(tempdict) 
                    if board[y][x] in tempdict:
                        if board[y][x] != 0:
                            #print("squarefail at " + str(y) + str(x))
                            return False
                    tempdict[board[y][x]] = 1
    return True


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

def checkChars(grid):
    dictionary  = {0: 0, 1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0}
    for y in range(9):
        for x in range(9):
            if grid[y][x] not in dictionary:
                #print(grid[y][x])
                return -1
            else:
                dictionary[(grid[y][x])] += 1
    sum = 0
    for i in range(1,10):
        sum += dictionary[i]
    return sum

def outputSudoku(grid):
    with open("solutions.txt", 'a') as f:
        f.write("Solutions: \n")
        for i in range(9):
            for j in range(9):
                f.write(str(grid[i][j]) + " ")
            f.write(" \n")
    f.close()

def inputSudoku():
    #print("hi")
    grid = []
    with open("input.txt", 'r') as f:
        for line in f:
            grid.append(line)
    i = 0
    #print(grid)
    while i < len(grid):
        grid[i] = str(grid[i]).split()
        #print(grid[i])
        i += 1
    #print(grid)
    if len(grid) != 9:
        return False
    if len(grid[0]) != 9:
        return False
    for y in range(9):
        for x in range(9):
            if grid[y][x] == '.':
                grid[y][x] = 0
            else:
                grid[y][x] = int(grid[y][x])
    #print(grid)
    thingy = checkChars(grid)
    #print(thingy)
    if thingy < 0:
        print("Error in grid!\n")
        return False
    if thingy < 17:
        print("Multiple solutions may exist. Please check your grid.\n")
    truthiness = isValidSudoku(grid)
    if not truthiness:
        print("Invalid sudoku!\n")
        return False
    return grid


def solve(grid, counter):
    #if counter > 100:
    #    return
    for y in range(9):
        for x in range(9):
            if grid[y][x] == 0:
                for n in range(1,10):
                    if isPossible(y,x,n, grid):
                        grid[y][x] = n
                        if counter < 81:
                            solve(grid, counter + 1)
                        grid[y][x] = 0
                return
    print("hi")
    outputSudoku(grid)
    print(np.matrix(grid))
    #print(3/0)
    sys.exit()
    #input("hello")


def inToOut():
    grid = inputSudoku()
    print(grid)
    if grid != False:
        solve(grid, 0)

inToOut()