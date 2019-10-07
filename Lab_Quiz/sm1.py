def DrawTSquareV(n):
    for i in range(n):
        print('*'*4)
        print('*  *')
        print('*  *')
    print('*'*4)

def DrawTSquareH(n):
    print('*'*(3*n+1))
    print('*  '*(n)+'*')
    print('*  '*(n)+'*')
    print('*'*(3*n+1))

mode = input('Select Mode (v or h): ')
n = int(input('Input n (1-15): '))

if mode == 'v':
    DrawTSquareV(n)
elif mode == 'h':
    DrawTSquareH(n)
    
