def getAbsolute(ss):
    res = 0
    for i in range(len(ss)):
        for j in range(len(ss[0])):
           res += ss[i][j]
    res /= len(ss)**2
    return res

def getAveragePlate(grid):
    dicP = {'A':0,'B':0,'C':0,'-':0}
    for i in range(len(grid)):
        for key,val in dic.items():
            if grid[i] > val: dicP[key] += 1
    return dicP

size = int(input('Material size: '))
grid = list()
absList = list()
dic = {'A':85,'B':70,'C':60,'-':0}
plateList = list()

for _ in range(size):
    inp = [int(x) for x in input().split()]
    for x in inp: plateList.append(x)
    grid.append(inp)
upgradeDic = getAveragePlate(plateList)

for row in range(0,size-2):
    for col in range(0,size-2):
        subSquare = list()
        for n in range(3): subSquare.append(grid[row:row+3][n][col:col+3])
        absList.append(getAbsolute(subSquare))
gradeDic = getAveragePlate(absList)
currentGrade = max(gradeDic,key=gradeDic.get)
avgPlate = size**2*25/100

for key,val in upgradeDic.items():
    if val > avgPlate:
        maxUpgrade = key
        break
    
if ord(currentGrade) > ord(maxUpgrade):
    print(f'Grade {maxUpgrade}(Upgrade from {currentGrade})')
else:
    print(f'Grade {currentGrade}')
#print(upgradeDic,gradeDic)
