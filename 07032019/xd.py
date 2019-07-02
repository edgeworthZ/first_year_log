a = 1
b = 0
n = int(input('Enter n: '))
if(n <= 1):
    print(1)
else:
    for i in range(2,n+1):
        tmp = a
        a = a+b
        b = tmp
        print(a)
    print(a)
