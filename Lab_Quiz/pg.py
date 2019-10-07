a = [1,2,3,3]
b = [4,5,6]
c = [a,b]
d = a,b

def isEven(n):
    if n%2 == 0:
        return n

A = [[1,2,3],
     [4,5,6],
     [8,8,9]]

B = [[3,1,0],
     [2,4,2],
     [4,7,3]]

B = filter(isEven, [1,2,3,4])
print(list(B))
print(a.count(3))
