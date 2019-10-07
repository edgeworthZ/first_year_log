def InverseMatrix(aa):
    a = aa[:]
    res = [[0 if row != col else 1 for col in range(len(a))] for row in range(len(a))]
    for j in range(len(a[0])-1):
        for i in range(len(a)-1,j,-1):
            coeff = a[i][j]/a[j][j]
            for k in range(len(a[0])):
                a[i][k] = a[i][k]-a[j][k]*coeff
                res[i][k] = res[i][k]-res[j][k]*coeff
    for i in range(len(a)):
        coeff = a[i][i]
        for j in range(len(a[0])):
            a[i][j] = a[i][j]/coeff
            res[i][j] = res[i][j]/coeff
    for j in range(len(a[0])-1,0,-1):
        for i in range(j):
            coeff = a[i][j]/a[j][j]
            for k in range(len(a[0])):
                a[i][k] = a[i][k]-a[j][k]*coeff
                res[i][k] = res[i][k]-res[j][k]*coeff
    return res

def diagOne(aa):
    a = aa[:]
    for i in range(len(a)):
        coeff = a[i][i]
        for j in range(len(a[0])):
            a[i][j] = a[i][j]/coeff
    return a

def printMat(aa):
    for r in aa:
        for c in r:
            print(f'{c:.2f}',end = ' ')
        print()

def mulMat(a,b):
    return [[sum(a*b for a,b in zip(rowA,colB)) for colB in zip(*b)] for rowA in a]

def addMat(a,b):
    return [[a+b for a,b in zip(*z)] for z in zip(a,b)]

def subMat(a,b):
    return [[a-b for a,b in zip(*z)] for z in zip(a,b)]

aa = [[1,2,3],
      [4,5,6],
      [7,2,9]]

printMat(subMat(aa,aa))
#printMat(aa)
#printMat(InverseMatrix(aa))
#printMat(mulMat(aa,InverseMatrix(aa)))
