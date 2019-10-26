class matrix():
    members = list()
    def __init__(self,mat):
        self.mat = [row[:] for row in mat[:]] # Clone matrix
        self.shape = (len(mat),len(mat[0])) # (row x col)
        self.size = self.shape[0]*self.shape[1] # Size of the matrix
        matrix.members.append(self) # Register this matrix instance to the class

    def __add__(self,other):
        res = matrix(self.mat)
        for i in range(len(res.mat)):
            for j in range(len(res.mat[0])):
                res.mat[i][j] += other.mat[i][j]
        return res

    def __sub__(self,other):
        res = matrix(self.mat)
        for i in range(len(res.mat)):
            for j in range(len(res.mat[0])):
                res.mat[i][j] -= other.mat[i][j]
        return res

    def __mul__(self,other):
        if type(other) == type(self): # Multiply matrix
            return matrix([[sum(a*b for a,b in zip(col_B,row_A)) for col_B in zip(*other.mat)] for row_A in self.mat])
        elif type(other) == (int or float): # Multiply constant number
            return matrix([[col*other for col in row] for row in self.mat])

    def __pow__(self,other):
        if other == -1: # Inverse Matrix
            return self.inverse_matrix()
        elif type(other) == int: # Power matrix
            res = matrix(self.mat)
            for i in range(other-1):
                res = res*self
            return res
        elif other in 'Tt': # Tranpose matrix
            return matrix([[col for col in row] for row in zip(*self.mat)])

    def inverse_matrix(self):
        # Clone Matrix
        a = [row[:] for row in self.mat[:]]
        # Identity Matrix
        aa = matrix.identity((self.shape[0],self.shape[1]))
        aiv = aa.mat
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
        return aa

    def zeros(shape):
        return matrix([[0 for col in range(shape[1])] for row in range(shape[0])])

    def ones(shape):
        return matrix([[1 for col in range(shape[1])] for row in range(shape[0])])

    def identity(shape):
        return matrix([[1 if col==row else 0 for col in range(shape[1])] for row in range(shape[0])])

    def arange(start,end,step):
        return matrix([[col for col in range(start,end,step)]])

    def print(self): # Print matrix
        for row in self.mat:
            for col in row:
                print(f'{col:>6}',end=' ')
            print()
    
a = [[1,2],[3,4]]
b = [[5,6],[7,8]]
t = 't'
A = matrix(a)
B = matrix(b)
formulas = {'A':A,
            'B':B,
            'A+B':A+B,
            'A-B':A-B,
            'A*2':A*2,
            'B**t':B**t,
            'A*B':A*B,
            'A**-1 (Inverse of A)':A**-1,
            'A*A**-1 (A X Inverse of A)':A*A**-1,
            'matrix zeros(2x2)':matrix.zeros((2,2)),
            'matrix ones(2x2)':matrix.ones((2,2)),
            'matrix identity(2x2)':matrix.identity((2,2)),
            '(A**2 + matrix.ones((2,2))) + (B*3)**t - A**-1':(A**2 + matrix.ones((2,2))) + (B*3)**t - A**-1}

for key,val in formulas.items():
    print(f'Result of {key}:')
    val.print()
    print('----------------')
    
#for mat in matrix.members: print(mat.__dict__)
