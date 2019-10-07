def diagOne(AA):
    A = AA[:]
    for i in range(len(A)):
        coeff = A[i][i]
        for j in range(len(A[0])):
            A[i][j] = A[i][j]/coeff
    return A

def lowerTriangle(AA):
    A = AA[:]
    for j in range(0,len(A[0])-1):
        for i in range(len(A)-1,j,-1):
            coeff = A[i][j]/A[j][j]
            for k in range(len(A[0])):
                A[i][k] = A[i][k]-A[j][k]*coeff
    A = diagOne(A)
    return A

def upperTriangle(AA):
    A = AA[:]
    for j in range(len(A[0])-1,0,-1):
        for i in range(0,j):
            coeff = A[i][j]/A[j][j]
            for k in range(len(A[0])):
                A[i][k] = A[i][k]-A[j][k]*coeff
    A = diagOne(A)
    return A

def inverseMatrix(aa):
    # Clone Matrix
    a = aa[:]
    # Identity Matrix
    aiv = [[1 if col==row else 0 for col in range(len(A[0]))] for row in range(len(A))]
    # Lower Triangle
    for j in range(0,len(a[0])-1):
        for i in range(len(a)-1,j,-1):
            coeff = a[i][j]/a[j][j]
            for k in range(len(a[0])):
                a[i][k] = a[i][k]-a[j][k]*coeff
                aiv[i][k] = aiv[i][k]-aiv[j][k]*coeff
    # DiagOne
    for i in range(len(a)):
        coeff = a[i][i]
        for j in range(len(a[0])):
            a[i][j] = a[i][j]/coeff
            aiv[i][j] = aiv[i][j]/coeff
    # Upper Triangle
    for j in range(len(a[0])-1,0,-1):
        for i in range(0,j):
            coeff = a[i][j]/a[j][j]
            for k in range(len(a[0])):
                a[i][k] = a[i][k]-a[j][k]*coeff
                aiv[i][k] = aiv[i][k]-aiv[j][k]*coeff
    return aiv

def multiply_Matrix(A,B):
    return [[sum(a*b for a,b in zip(A_row,B_col)) for B_col in zip(*B)] for A_row in A]

def PrintMatrix(M):
    for row in M:
        for col in row:
            if round(col,2) == round(col):
                print(f'{round(col):>7}', end ='')
            else:
                print(f'{col:>7.2g}', end ='')
        print()

A = [[1,2,3],
     [4,5,6],
     [7,2,9]]

PrintMatrix(A)
PrintMatrix(inverseMatrix(A))
PrintMatrix(multiply_Matrix(A,inverseMatrix(A)))
