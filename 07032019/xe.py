num1 = int(input('Input number 1: '))
num2 = int(input('Input number 2: '))
if(num1 > 0 and num2 > 0):
    maxi = num2
    mini = num1
    if(num1 > num2):
        maxi = num1
        mini = num2
    maxi = maxi % mini
    while(maxi != 0):
        if(mini > maxi):
            tmp = maxi
            maxi = mini
            mini = tmp
        maxi = maxi % mini
    print(mini)
else:
    print('Number 1 or 2 is less than 0.')
