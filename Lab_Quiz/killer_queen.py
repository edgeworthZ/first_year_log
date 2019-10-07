def straight(vector):
    i,j = vector[0],vector[1]
    while(True):
        if (queen_x+i,queen_y+j) in others: break
        if -1 < queen_x+i < len(x) and -1 < queen_y+j < len(x[0]):
            x[queen_x+i][queen_y+j] = 'X'
        else: break
        i,j = i+vector[0],j+vector[1]

def diag(vector):
    vectorX,vectorY = vector[0],vector[1]
    for i in range(1,len(x)):
        if (queen_x+i*vectorX,queen_y+i*vectorY) in others: break
        if -1 < queen_x+i*vectorX < len(x) and -1 < queen_y+i*vectorY < len(x[0]):
            x[queen_x+i*vectorX][queen_y+i*vectorY] = 'X'

#Initialization
x=[['O' for col in range(8)] for row in range(8)]
dic = {'a':1,'b':2,'c':3,'d':4,'e':5,'f':6,'g':7,'h':8}
queen = input("Queen's Position: ")
queen_x,queen_y = 8-int(queen[1]),dic[queen[0]]-1
others = list()
while(True):
    o = input("Other's Position: ")
    if len(o) < 1: break
    others.append((8-int(o[1]),dic[o[0]]-1))
#Try navigating
[straight(param) for param in [(0,1),(0,-1),(1,0),(-1,0)]]
[diag(param) for param in [(-1,1),(-1,-1),(1,1),(1,-1)]]
#Masking
x[queen_x][queen_y] = 'Q'
for e in others: x[e[0]][e[1]] = 'P'
for r in x: print(*r)
