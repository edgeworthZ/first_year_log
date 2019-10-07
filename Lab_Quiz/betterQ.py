class Pos(): #(x,y)
    x,y = 0,0
    def __init__(self,x,y):
        self.x,self.y = x,y
        
class Vector2(): #U = Up, D = Down, L = Left, R = Right
    U,D,L,R = Pos(0,1),Pos(0,-1),Pos(-1,0),Pos(1,0)
    UL,UR,DL,DR = Pos(-1,1),Pos(1,1),Pos(-1,-1),Pos(1,-1)

class Pawn():
    short,reach,paths = '',0,list()
    def __init__(self,short,reach,paths):
        self.short,self.reach,self.paths = short, reach, paths

def Navigate(fromRow, fromCol, direction, reach, allowEating = False):
    step = 0
    while(step < reach):
        fromRow,fromCol = fromRow-direction.y,fromCol+direction.x # Use direction vector to move from current position
        if not -1 < fromRow < size or not -1 < fromCol < size: # Stop if it hits the border
            break
        if grid[fromRow][fromCol] == 0 or grid[fromRow][fromCol] == 'X' or allowEating: # Is this space empty?
            grid[fromRow][fromCol] = 'X'
            if allowEating: break # It eats some pawn, stop.
        else: # It hits something, stop.
            break
        step += 1
import re

size = int(input("Board Size: ")) # Board's Size
grid=[[0 for col in range(size)] for row in range(size)] # Empty Board
dic = {chr(ord('a')+num%26)*(1+num//26):num+1 for num in range(size)} # Column indexing
dicP = {'King': Pawn('K',1,[Vector2.R,Vector2.L,Vector2.U,Vector2.D,Vector2.UR,Vector2.UL,Vector2.DR,Vector2.DL]),
        'Queen':Pawn('Q',size,[Vector2.R,Vector2.L,Vector2.U,Vector2.D,Vector2.UR,Vector2.UL,Vector2.DR,Vector2.DL]),
        'Knight': Pawn('J',1,[Pos(2,1),Pos(2,-1),Pos(-2,1),Pos(-2,-1),Pos(1,2),Pos(-1,2),Pos(1,-2),Pos(-1,-2)])}

king = input("King's Position: ") # Get king's position
king = re.split(r'(\d+)',king) # Split by using 1 or more digit(s) as a spliter (For board larger than 26x26)
king_pos = Pos(size-int(king[1]),dic[king[0]]-1) # Register queen's position in Pos (x,y)
grid[king_pos.x][king_pos.y] = 'K' # Place queen on board
while(True): # Get enemy' position and place them on the board
    enemy_name = input("Pawn's Type(Queen,Knight): ")
    if len(enemy_name) < 1:
        break
    enemy = input(f"{enemy_name}'s Position: ")
    enemy = re.split(r'(\d+)',enemy)
    enemy_pos = Pos(size-int(enemy[1]),dic[enemy[0]]-1)
    grid[enemy_pos.x][enemy_pos.y] = dicP[enemy_name].short # Place pawn on the board
    for path in dicP[enemy_name].paths: # Navigate the pawn to each of its paths, starting from its position
        Navigate(enemy_pos.x,enemy_pos.y,path,dicP[enemy_name].reach)
for r in grid: # Print the board
    print(*r)

# Checkmate? --> Try navigating King, if King can't stamp any 'X' onto the board then it's a checkmate
oldGrid = [[grid[row][col] for col in range(len(grid[row]))] for row in range(len(grid))]
for path in dicP['King'].paths:
    Navigate(king_pos.x,king_pos.y,path,dicP['King'].reach, allowEating = True)
if oldGrid != grid: #King was able to move
    print(f"King can still move to",end = ' ')
    escapeList = list()
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] != oldGrid[row][col]:
                escapeList.append(chr(col+ord('a'))+str(size-row))
    for pos in sorted(escapeList):
        print(pos, end=' ')
    print()
else:
    print("Checkmate!")
