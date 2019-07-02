x,y = [float(x) for x in input('Enter point (x,y): ').split(',')]
if(x == 0 and y == 0):
    print(f'Point({x},{y}) is at the origin.')
elif(x == 0 and y != 0):
    print(f'Point({x},{y}) is on the y-axis.')
elif(x != 0 and y == 0):
    print(f'Point({x},{y}) is on the x-axis.')
else:
    if(x > 0 and y > 0):
        print(f'Point({x},{y}) is in quadrant 1.')
    elif(x < 0 and y > 0):
        print(f'Point({x},{y}) is in quadrant 2.')
    elif(x < 0 and y < 0):
        print(f'Point({x},{y}) is in quadrant 3.')
    elif(x > 0 and y < 0):
        print(f'Point({x},{y}) is in quadrant 4.')
