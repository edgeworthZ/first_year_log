def IsSudokuValid(line, cType):
    if(sum(line[1]) == sum(set(line[1]))): # This line is safe
        return True
    else: # Something is wrong, find duplicate numbers' locations
        for n in [1,2,3,4,5,6,7,8,9]:
            if line[1].count(n) > 1: # Found duplicate
                for i in range(len(line[1])): # Get index of each duplicate number
                    if line[1][i] == n:
                        if cType == 'row':
                            #print('row:',line[0],'col:',i+1)
                            res.add(chr(ord('A')-1+line[0])+str(i+1))
                        elif cType == 'col':
                            res.add(chr(ord('A')-1+(i+1))+str(line[0]))
        return False

def CheckSudoku(grid):
    wrongRows = [row for row in enumerate(grid, 1) if not IsSudokuValid(row, 'row')] # Check Rows
    transposedGrid = list(zip(*grid))
    wrongCols = [col for col in enumerate(transposedGrid, 1) if not IsSudokuValid(col, 'col')] # Check Cols
    squares = []
    for i in range(0,9,3): # Check Squares
        for j in range(0,9,3):
            square = list(col for rows in grid[i:i+3] for col in rows[j:j+3])
            #print(square)
            squares.append(square)
    wrongSquares = [square for square in enumerate(squares, 1) if not IsSudokuValid(square, 'square')]
    return not(wrongRows or wrongCols or wrongSquares)

grid = list()
res = set()
for i in range(9):
    grid.append([int(x) for x in input().split()])
if CheckSudoku(grid):
    print('Correct!')
else:
    print('Incorrect!')
    print(*sorted(res))
