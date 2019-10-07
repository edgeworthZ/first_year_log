m,n = [int(x) for x in input('Grid Size: ').split()]
mns = int(input('Number of mine(s): '))
mns_ls = list()
for i in range(mns):
    mns_ls.append([int(x) for x in input(f'Mine#{i}: ').split()])
grid = list()
for i in range(m):
    row = list()
    for j in range(n):
        if [i,j] in mns_ls:
            row.append('X')
        else:
            nearBomb = 0
            for k in range(-1,2):
                for l in range(-1,2):
                    if [i+k,j+l] in mns_ls:
                        nearBomb += 1
            row.append(nearBomb)
    grid.append(row)
for row in zip(*grid):
    print(*row)
