from os import listdir
from itertools import *

SUDOKU_PATH = 'sudoku'

def IsSudokuValid(line, cType):
    if(sum(line[1]) == sum(set(line[1]))):
        return True
    else:
        print('Wrong',cType,'at',cType,'No.',line[0])
        return False

def SudokuText2Grid(fileName):
    f = open(SUDOKU_PATH+'/'+fileName)
    grid = []
    while True:
        line = f.readline()
        if not line:
             break
        grid.append([int(x) for x in line.split()])
    return grid

def CheckSudoku(grid):
    wrongRows = [row for row in enumerate(grid, 1) if not IsSudokuValid(row, 'row')]
    transposedGrid = list(zip(*grid))
    wrongCols = [col for col in enumerate(transposedGrid, 1) if not IsSudokuValid(col, 'col')]
    squares = []
    for i in range(0,9,3):
        for j in range(0,9,3):
            square = list(col for rows in grid[i:i+3] for col in rows[j:j+3])
            print(square)
            squares.append(square)
    wrongSquares = [square for square in enumerate(squares, 1) if not IsSudokuValid(square, 'square')]
    return not(wrongRows or wrongCols or wrongSquares)

for fileName in listdir(SUDOKU_PATH):
    grid = SudokuText2Grid(fileName)
    print(fileName,'is a valid sudoku.') if CheckSudoku(grid) else print(fileName,'is not a valid sudoku.')
