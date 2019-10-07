def FireSaitron(startRow,startCol,toRow,toCol):
    #print(startRow,startCol,toRow,toCol)
    saiRow,saiCol = startRow,startCol
    n = 0
    while(True):
        if grid[saiRow][saiCol] == '/': # Did saitron crash with a barrier?
            #print('Bounce1!')
            n+=1
            toRow,toCol = -toCol,-toRow
        elif grid[saiRow][saiCol] == '\\':
            #print('Bounce2!')
            toRow,toCol = toCol,toRow
            n+=1
        # Did saitron crash with a border?
        if -1 < saiRow+toRow < len(grid) and -1 < saiCol+toCol < len(grid[0]):
            saiRow,saiCol = saiRow+toRow,saiCol+toCol
            #print('goto',saiRow,saiCol)
        else:
            break
    return 2**n


grid,particles  = list(),list()
while(True):
    s = input()
    if len(s) > 0:
        s = s.split()
        grid.append(s)
    else:
        break

for i in range(len(grid)): # Loop row
    particles.append(FireSaitron(i,0,0,1)) # Fire to Right
    particles.append(FireSaitron(i,len(grid[i])-1,0,-1)) # Fire to Left
grid_trans = list(zip(*grid)) # Tranpose
for j in range(len(grid[0])): # Loop column
    particles.append(FireSaitron(0,j,1,0)) # Fire to Down
    particles.append(FireSaitron(len(grid)-1,j,-1,0)) # Fire to Up
print(f'Maximum saitron is {max(particles)} particle(s)')

'''
\ 0,1 -> 1,0
\ 0,-1 -> -1,0
\ 1,0 -> 0,1
\ -1,0 -> 0,-1

/ 0,1 -> -1,0
/ 0,-1 -> 1,0
/ 1,0 -> 0,-1
/ -1,0 -> 0,1'''
