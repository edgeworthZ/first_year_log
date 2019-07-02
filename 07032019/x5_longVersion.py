a,b,c = [int(x) for x in input('Enter 3 numbers: ').split()]
if(a<b):
    if(a<c):
        minNum = a
    else:
        minNum = c
elif(b<c):
    minNum = b
else:
    minNum = c
            
print(f'Mininum number is {minNum}')
