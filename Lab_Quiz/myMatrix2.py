A = [[1,2,3],
     [4,5,6],
     [8,8,9]]

B = [[3,1,0],
     [2,4,2],
     [4,7,3]]

def AddMatrix(A,B):
    result = []
    for t in zip(A,B):
        result.append(list(map(sum,zip(*t))))
    print('Add',result)

def SubMatrix(A,B):
    result = []
    for t in zip(A,B):
        result.append(list(map(lambda x: x[0]-x[1], zip(*t))))
    print('Substract',result)

def MultiplyNumMatrix(n,A):
    result = [[n*col for col in row] for row in A]
    print('MultiplyNumber',result)

def CrossMatrix(A,B):
    result = [[sum(a*b for a,b in zip(A_row, B_col)) for B_col in zip(*B)] for A_row in A]
    print('Cross', result)

def TransposeMatrix(A):
    result = list(zip(*A))
    print('Transpose',result)

print('A',A)
print('B',B)
AddMatrix(A,B)
SubMatrix(A,B)
MultiplyNumMatrix(2,A)
CrossMatrix(A,B)
TransposeMatrix(A)
