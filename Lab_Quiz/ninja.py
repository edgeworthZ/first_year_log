def TryMove(nextGrid,shuriken,i,j):
    vectorI,vectorJ = 0,0
    
    if nextGrid[i][j] == shuriken:
        nextGrid[i][j] = '-'
        
    if shuriken == 'r': vectorJ = 1
    elif shuriken == 'l': vectorJ = -1
    elif shuriken == 'a': vectorI = -1
    elif shuriken == 'b': vectorI = 1
        
    if not -1 < i+vectorI < len(nextGrid) or not -1 < j+vectorJ < len(nextGrid[0]): # Hit with border
        return nextGrid
    
    if nextGrid[i+vectorI][j+vectorJ] == '-': # No obstacle -> move
        #print(shuriken,'move1!')
        nextGrid[i+vectorI][j+vectorJ] = shuriken
        footsteps[i+vectorI][j+vectorJ] = 'x'
        return nextGrid
    else: # Move into an obstacle
        if vectorI < 0 or vectorJ  < 0: # Don't crash with a shuriken that still doesn't move
            #print(shuriken, 'Crashed Type-I: Shuriken crash with old one.')
            grid[i+vectorI][j+vectorJ] = '-' # Destroy shuriken
            nextGrid[i+vectorI][j+vectorJ] = '-'
            return nextGrid
        elif nextGrid[i+vectorI][j+vectorJ]+shuriken in ['rl','lr','ab','ba']:
            #print(shuriken, 'Crashed Type-II: Shuriken crash with new one.')
            grid[i+vectorI][j+vectorJ] = '-' # Destroy shuriken
            nextGrid[i+vectorI][j+vectorJ] = '-'
            return nextGrid
        else:
            #print(shuriken,'move2!')
            nextGrid[i+vectorI][j+vectorJ] = shuriken
            footsteps[i+vectorI][j+vectorJ] = 'x'
            return nextGrid

w = int(input('W: '))
h = int(input('H: '))
n = int(input('N: '))
grid = [['-' for col in range(w)] for row in range(h)]
footsteps = [['o' for col in range(w)] for row in range(h)]
for i in range(4,4+n,1):
    x,y,d = input().split()
    x,y = int(x),int(y)
    grid[y-1][x-1] = d
    footsteps[y-1][x-1] = 'x'
'''for g in grid: print(*g)'''
while(True):
    #print('New Turn')
    #for g in grid: print(*g)
    shouldContinue = False
    nextGrid = [list(row) for row in grid]
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] != '-':
                nextGrid = TryMove(nextGrid,grid[i][j],i,j)
                '''for g in nextGrid: print(*g)'''
    if all(all(col == '-' for col in row) for row in nextGrid): # Stop when there's no shuriken left
        break
    grid = nextGrid
'''for t in footsteps: print(*t)'''
print(sum(sum(col == 'x' for col in row) for row in footsteps)) # Count all footsteps
