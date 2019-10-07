x = int(input('x: '))
y = int(input('y: '))

if(y//24>0):
        x += y%24
else:
        x += y

if(x//24>0):
        x -= 24

print(f'She comes at {x}:00')
