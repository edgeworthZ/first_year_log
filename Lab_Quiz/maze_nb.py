def printMat(A):
    for r in zip(*A):
        print(*r)

def diag(x,n,si,sj):
    vectorX,vectorY = 1,1
    if (si+sj)% 2 != 0:
        pattern = reversed(range(len(x)))
    else:
        pattern = range(len(x))
    for i in pattern:
        if -1 < si+i*vectorX < len(x) and -1 < sj+i*vectorY < len(x[0]):
            x[si+i*vectorX][sj+i*vectorY] = n
            n+=1
    return x,n

def p1():
    p1 = [[col+1+row*size for col in range(size)] for row in range(size)]
    printMat(p1)

def p2():
    p2 = [[col+1+row*size for col in range(size)][::(-1)**row] for row in range(size)]
    printMat(p2)

def p3():
    p3 = [[0 for col in range(size)] for row in range(size)]
    n = 1
    for i in range(size-1,-1,-1):
        p3,n = diag(p3,n,i,0)
    for j in range(1,size,1):
        p3,n = diag(p3,n,0,j)
    printMat(zip(*p3))

def p4():
    p4 = [[0 for col in range(size)] for row in range(size)]
    pat=[(1,0),(0,1),(-1,0),(0,-1)]
    n,i,j = 1,0,0
    cur = (-1,0)
    while(n < size**2+1):
        dir = pat[i%4]
        dis = size-j
        for k in range(dis):
            cur = (cur[0]+dir[0],cur[1]+dir[1])
            p4[cur[0]][cur[1]] = n
            n+=1
        if i%2 == 0 or i == 0 and i > 0:
            j+=1
        i+=1
    printMat(zip(*p4))

size = int(input('Input size: '))
pat = int(input('Pattern: '))
fdic = {1:p1,2:p2,3:p3,4:p4}
fdic[pat]()
