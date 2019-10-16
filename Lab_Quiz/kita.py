r = int(input('R: '))
c = int(input('C: '))
grid = [[0 for col in range(c)] for row in range(r)]
res = 0
maxSq = min(r,c)
for s in range(0,maxSq+1):
    for i in range(0,len(grid)-s,1):
        for j in range(0,len(grid[0])-s,1):
            res += 1
print(res)
