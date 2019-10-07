def MinorMatrix(M,i,j):
    return [row[:j]+row[j+1:] for row in M[:i]+M[i+1:]]
def Minor(M,i,j):
    return Det(MinorMatrix(M,i,j))

def Det(M): #Find Determinant by Laplace Expansions
    if len(M) == 1:
        return M[0][0]
    else:
        return sum([(-1)**col*M[0][col]*Minor(M,0,col) for col in range(len(M))])

A = list()
for i in range(3):
    row = [int(x) for x in input(f'Row {i+1} : ').split()]
    A.append(row)
print(Det(A))
