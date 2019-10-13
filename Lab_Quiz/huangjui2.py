def BuyIn(sqq):
    sq = [x for x in sqq] # Clone square
    price = 0
    for i in range(len(sq)):
        price += sq[i]
        if i+1 < len(sq):
            sq[i-1],sq[i+1] = sq[i-1]*1.1,sq[i+1]*1.1
    return price

grid = list()
res = list()
while(True):
    row = [int(x) for x in input().split()]
    if len(row) < 1:
        break
    grid.append(row)
for i in range(len(grid)-1):
    for j in range(len(grid[0])-1):
        subSquare = grid[i:i+2][0][j:j+2]+grid[i:i+2][1][j:j+2]
        cwSquare = subSquare[:2]+subSquare[2:][::-1] 
        res.append(BuyIn(cwSquare)) # Clockwise
        res.append(BuyIn(cwSquare[::-1])) # Counter Clockwise
print(f'{min(res):.10g}')
