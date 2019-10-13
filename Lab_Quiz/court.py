l = int(input('Length: '))
w = int(input('Width: '))
field,courts = list(),list()
courtsCount = 0
for i in range(l):
    field.append([int(x) for x in input().split()])
for i in range(l-4):
    for j in range(w-2):
        spaces = 0
        entry = [list(row) for row in field] # Clone field
        for _i in range(4):
            for _j in range(2):
                if entry[i+_i][j+_j] == 1:
                    entry[i+_i][j+_j] = 'x'
                    spaces += 1
        if spaces > 7:
            courts.append(entry)
            courtsCount += 1
print(f'{courtsCount} possible court(s)')
for court in courts:
    for row in court:
        print(*row)
    print()
