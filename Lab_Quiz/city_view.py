def Raycast(line):
    building = 1
    i,j = 0,1
    while(i+j < len(line)-1):
        if line[i] < line[i+j]:
            building += 1
            i += 1
            j = 1
        else:
            j += 1
            continue
    return building

cs = [int(x) for x in input('City Size: ').split()]
grid = list()
for row in range(cs[0]):
    grid.append([int(x) for x in input().split()])
    
Orth = {'N':0,'S':0,'E':0,'W':0}
Orth['W'] = sum([Raycast(row) for row in grid])
Orth['E'] = sum([Raycast(row[::-1]) for row in grid])
Orth['N'] = sum([Raycast(row) for row in zip(*grid)])
Orth['S'] = sum([Raycast(row[::-1]) for row in zip(*grid)])

for key,val in Orth.items():
    if val == max(Orth.items())[1]:
        print(key,end=' ')
print()
