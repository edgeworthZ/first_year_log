def mul_const(M,n):
    return [[col*n for col in row] for row in M]
def transpose_matrix(M):
    return [[col for col in row] for row in zip(*M)]
def plus_matrix(A,B):
    return [[sum(col) for col in zip(*z)] for z in zip(A,B)]
def minus_matrix(A,B):
    return [[col[0]-col[1] for col in zip(*z)] for z in zip(A,B)]
def mul_matrix(A,B):
    return [[sum(a*b for a,b in zip(col_B,row_A)) for col_B in zip(*B)] for row_A in A]
def power_matrix(A,c):
    mask = A[:]
    for i in range(c-1):
        mask = mul_matrix(mask,mask)
    return mask
def PrintMatrix(M):
    for row in M:
        for col in row:
            print(f'{col:>6}',end=' ')
        print()

A = [[1,2],[3,4],[5,6]]
B = [[7,9,11],[8,10,12]]
C = [[13,14],[15,16]]
D = [[100,50],[20,70]]

step1 = plus_matrix(A,transpose_matrix(B))
step2 = minus_matrix(power_matrix(C,2),D)
step3 = mul_matrix(step1,step2)
PrintMatrix(step3)
