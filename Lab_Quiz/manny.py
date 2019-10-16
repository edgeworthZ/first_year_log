u = int(input('Number of urinals: '))
grid = ['-' for x in range(u)]
man,manny,unknown = 0,0,0
while(True):
    txt = input()
    if txt == 'end':
        break
    entry = txt.split()
    if len(entry) > 1: # We need a valid number
        n = int(entry[1])-1
    if entry[0] == 'in':
        # Check Toilet Checkmate
        safeZone = grid[:]
        for room in range(len(safeZone)):
            if safeZone[room] == 'x':
                if -1 < room-1:
                    safeZone[room-1] = 'n'
                if room+1 < len(safeZone):
                    safeZone[room+1] = 'n'
        #print('sz',*safeZone)
        if '-' in safeZone:
            thereIsStillHope = True
            #print('ThereIsStillHope')
        else:
            thereIsStillHope = False
            #print('CheckMate!')

        # Check Empty Toilet
        if not 'x' in grid or not thereIsStillHope :
            unknown += 1
            grid[n] = 'x'
        else:
            foundX = False
            grid[n] = 'x'
            if -1 < n-1:
                if grid[n-1] == 'x':
                    foundX = True
            if n+1 < len(grid):
                if grid[n+1] == 'x':
                    foundX = True
            if foundX:
                manny += 1
            else:
                man += 1
    if entry[0] == 'out':
        grid[n] = '-'
    #print(*grid)
print(f'Total: {man+manny+unknown}')
print(f'Man: {man}')
print(f'Manny: {manny}')
print(f'Unknown: {unknown}')
