from os import listdir
from itertools import *

SUDOKU_PATH = 'sudoku'

def GetSudokuFiles():
    return listdir(SUDOKU_PATH)

def SudokuTextToGrid(fileName):
    grid = []
    f = open(SUDOKU_PATH+'/'+fileName)
    while True:
        line = f.readline()
        if not line:
            break
        grid.append([int(x) for x in line.split()])
    return grid

def IsSudokuOrdinal(line, rType):
    if(sum(line[1]) == sum(set(line[1]))):
        return True
    else:
        print('Wrong',rType,'at',rType,':',line[0])
        return False

def CheckSudoku(grid):
    wrongRows = [row for row in enumerate(grid, 1) if not IsSudokuOrdinal(row, 'row')]
    transGrid = list(zip(*grid))
    wrongCols = [col for col in enumerate(transGrid, 1) if not IsSudokuOrdinal(col, 'column')]
    squares = []
    for i in range(0,9,3):
        for j in range(0,9,3):
            square = list(chain(*list(row[j:j+3] for row in grid[i:i+3])))
            squares.append(square)
    wrongSquares = [square for square in enumerate(squares, 1) if not IsSudokuOrdinal(square, 'square')]
    return not (wrongRows or wrongCols or wrongSquares)

for fileName in GetSudokuFiles():
    print(f'...Begin checking {fileName}')
    grid = SudokuTextToGrid(fileName)
    print(fileName,'is a valid sudoku.\n') if CheckSudoku(grid) else print(fileName,'is not a valid sudoku.\n')
