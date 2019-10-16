def VectorToLetter(i,j):
    if i == 0 and j == 1: return 'E'
    elif i == 0 and j == -1: return 'W'
    elif i == 1 and j == 0: return 'S'
    elif i == -1 and j == 0: return 'N'
    return res

def Raycast(startI,startJ,directionI,directionJ,start,stop,step,res):
    for i in range(start, stop,step):
        if grid[startI+directionI*step][startJ+directionJ*step] == '2':
            #print('Found a way!')
            paths.append(res+VectorToLetter(directionI*step,directionJ*step))
            break
        elif grid[startI+directionI*step][startJ+directionJ*step] ==  'x':
            #print('Found x at',startI+directionI*step,startJ+directionJ*step)
            if i != start: # No need to consider surrounding 'x'
                ScanLocalXAxis(startI,startJ,directionJ,directionI,res+VectorToLetter(directionI*step,directionJ*step))
            break
        startI += directionI*step
        startJ += directionJ*step

def ScanLocalXAxis(worldPosI,worldPosJ,rotationI,rotationJ,res=''): # No need to check Z-Axis of player's local
    if rotationJ != 0: # Player's respective left and right are rows
        targetWorldPos = worldPosJ
        if rotationJ > 0: endBorder = len(grid)-1
        else: endBorder = -1
    else: # # Player's respective left and right are columns
        targetWorldPos = worldPosI
        if rotationI > 0: endBorder = len(grid[0])-1
        else: endBorder = -1
    Raycast(worldPosI,worldPosJ,rotationI,rotationJ,targetWorldPos, 0, -1,res) # Go Left
    Raycast(worldPosI,worldPosJ,rotationI,rotationJ,targetWorldPos, endBorder, 1,res) # Go Right

size = int(input('Size : '))
grid,paths = list(),list()
for row in range(size): # Get data from input
    col = [x for x in input().split()]
    if '1' in col: playerPosI,playerPosJ = row,col.index('1')
    grid.append(col)
ScanLocalXAxis(playerPosI,playerPosJ,1,0) # Scan Z-Axis
ScanLocalXAxis(playerPosI,playerPosJ,0,1) # Scan X-Axis
print(f'{len(paths)} possible way(s)')
for path in paths: print(*path)
