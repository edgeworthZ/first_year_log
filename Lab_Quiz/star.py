n = int(input().split('.')[0])

for i in range(n,0,-1):
    print('*'*i)
    
for i in range(0,n):
    print(' '*i+'*'*(n-i))

for i in range(1,n+1):
    print('*'*i)

for i in range(n-1,-1,-1):
    print(' '*i+'*'*(n-i))

x = ''
for i in range(n,0,-1):
    x += '*'*i+' '*(n-i)+' '*(n-i)+'*'*i+'\n'
for i in range(1,n+1):
    x += '*'*i+' '*(n-i)+' '*(n-i)+'*'*i+'\n'
print(x)
print(x.replace(' ','_').replace('*',' ').replace('_','*'))
