def LowerRight(c,i,j): # Navigate from current pos to lower left until it hits border
    while(i+1 < len(grid)): # Checking only row is enough, it won't hit column's border
        if c > len(txt)-2: break
        c,i,j = c+1,i+1,j+1
        grid[i][j] = txt[c]
    return c,i,j

def UpperRight(c,i,j): # Same as above, but different direction
    while(-1 < i-1): 
        if c > len(txt)-2: break
        c,i,j = c+1,i-1,j+1
        grid[i][j] = txt[c]
    return c,i,j

def Down(c,i,j): # Same as above, but different direction
    while(i < len(grid)-1):
        if c > len(txt)-2: break
        i,c = i+1,c+1
        grid[i][j] = txt[c]
    return c,i,j

def Up(c,i,j): # Same as above, but different direction
    while(i > 0):
        if c > len(txt)-2: break
        i,c = i-1,c+1
        grid[i][j] = txt[c]
    return c,i,j

txt = 'ZigzagHellIsTooEasyForMeBecauseIamAnPythonExpert'
size = 4
c,i,j = 0,0,0
grid = [['-' for col in range(len(txt))] for row in range(size)] # Correct amount of col can be calculated, but let's save time

grid[i][j] = txt[c] # Put the first character at (0,0)

while(c < len(txt)-1):
    c,i,j = Down(c,i,j)
    for k in range(2):
        c,i,j = UpperRight(c,i,j)
        c,i,j = LowerRight(c,i,j)
    c,i,j = Up(c,i,j)
    for k in range(2):
        c,i,j = LowerRight(c,i,j)
        c,i,j = UpperRight(c,i,j)

for row in grid:
    print(*row)

# To output text, just create string from each row and get rids of '-' in the lines.
    
''' ### Pattern ###
    Down()
    UpperRight()
    LowerRight()
    UpperRight()
    LowerRight()
    Up()
    LowerRight()
    UpperRight()
    LowerRight()
    UpperRight()
    Continue from the first-->
    ###############
    '''
