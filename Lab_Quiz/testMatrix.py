def IdenMat(n):
    return [[1 if col==row else 0 for col in range(n)] for row in range(n)]
def SequenceMat(n):
    return [[col+1+row*n for col in range(n)] for row in range(n)]
def MatTimesN(M,n):
    return [[col*n for col in row] for row in M]
def Tranpose(M):
    return [[col for col in row] for row in zip(*M)]
def AddMatrix(A,B):
    return [[sum(col) for col in zip(*z)] for z in zip(A,B)]
def SubMatrix(A,B):
    return [[col[0]-col[1] for col in zip(*z)] for z in zip(A,B)]
def MulMatrix(A,B):
    return [[sum(a*b for a,b in zip(col_B,row_A)) for col_B in zip(*B)] for row_A in A]
def Det(M): #Find Determinant by Laplace Expansions
    return M[0][0]if len(M) == 1 else sum([(-1)**col*M[0][col]*Minor(M,0,col) for col in range(len(M))])
def MinorMatrix(M,i,j):
    return [row[:j]+row[j+1:] for row in M[:i]+M[i+1:]]
def Minor(M,i,j):
    return Det(MinorMatrix(M,i,j))
def Cofactor(M):
    return [[(-1)**(row+col)*Minor(M,row,col) for col in range(len(M[row]))] for row in range(len(M))]
def Adj(M):
    return Tranpose(Cofactor(M))
def InverseMat(M):
    return MatTimesN(Adj(M),1/Det(M))
def PrintMatrix(M):
    for row in M:
        for col in row:
            if round(col,2) == round(col):
                print(f'{round(col):>7}', end ='')
            else:
                print(f'{col:>7.2g}', end ='')
        print()
def Output(header,statement): #Execute statement with decorations
    print('-'*50)
    print(header)
    print('-'*50)
    statement()
    print('-'*50)

A = [[4,0,2,3],
     [2,3,2,1],
     [3,0,1,1],
     [1,2,4,2]]

B = [[1,1,0,2],
     [1,3,1,3],
     [3,2,1,0],
     [2,1,0,4]]

'''A = [[4,7],
     [2,6]]

B = [[4,7],
     [2,6]]'''

Output('Identity Matrix',lambda:PrintMatrix(IdenMat(3)))
Output('Identity Matrix Multiply by N=2',lambda:PrintMatrix(MatTimesN(IdenMat(3),2)))
Output('Matrix A',lambda:PrintMatrix(A))
Output('Matrix B',lambda:PrintMatrix(B))
Output('Tranpose Matrix A',lambda:PrintMatrix(Tranpose(A)))
Output('Add Matrix A,B',lambda:PrintMatrix(AddMatrix(A,B)))
Output('Subtract Matrix A,B',lambda:PrintMatrix(SubMatrix(A,B)))
Output('Multiply Matrix A,B',lambda:PrintMatrix(MulMatrix(A,B)))
Output('Determinant of A',lambda:print(Det(A)))
Output('Minor Matrix A11',lambda:PrintMatrix(MinorMatrix(A,1,1)))
Output('Minor A11',lambda:print(Minor(A,1,1)))
Output('Cofactor Matrix A',lambda:PrintMatrix(Cofactor(A)))
Output('Adjugate Matrix A',lambda:PrintMatrix(Adj(A)))
Output('InverseMatrix A',lambda:PrintMatrix(InverseMat(A)))
Output('A Multiply by A_Inverse',lambda:PrintMatrix(MulMatrix(A,InverseMat(A))))
