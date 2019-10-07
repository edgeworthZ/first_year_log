from os import listdir

MATRIX_PATH = 'MATRIX'
matrixs = {}

A = [[1,2,3],
     [4,5,6],
     [7,8,9]]

B = [[5,2,12],
     [3,1,99],
     [1,3,8]]

def AddMatrix(A,B):
    result = []
    for t in zip(A,B):
        result.append(list(map(sum, list(zip(*t)))))
    print(result)

def SubMatrix(A,B):
    result = []
    for t in zip(A,B):
        result.append(list(map(lambda x: x[0]-x[1], list(zip(*t)))))
    print(result)

def MultiplyMatrix(A,B):
    result = [[sum(a*b for a,b in zip(A_row,B_col)) for B_col in zip(*B)] for A_row in A]
    print(result)

def MultiplyNumber2Matrix(n,A):
    result = list(map(lambda rows:[a*n for a in rows], A))
    print(result)

def TranposeMatrix(A):
    result = [list(a) for a in zip(*A)]
    print(result)

for file in enumerate(listdir(MATRIX_PATH),1):
    f = open(MATRIX_PATH+'/'+file[1])
    grid = []
    while True:
        line = f.readline()
        if not line:
            break
        grid.append([float(x) for x in line.split()])
    matrixs['matrix'+str(file[0])] = grid
AddMatrix(A,B)
SubMatrix(A,B)
MultiplyNumber2Matrix(2,A)
MultiplyMatrix(A,B)
TranposeMatrix(A)

