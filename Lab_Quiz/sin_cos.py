import math

def fact(n):
    fact = 1
    for i in range(1,n+1):
        fact = fact * i
    return fact

deg = float(input('Enter degree: '))
x = math.radians(deg)
cos_x = sum([((-1)**n)*(x**(2*n))/fact(2*n) for n in range(0,11)])
sin_x = sum([(-1)**(n-1)*x**(2*n-1)/fact(2*n-1) for n in range (1,11)])
print(f'degree: {deg}')
print(f'sin({deg}°): {round(sin_x,10):.10f}')
print(f'cos({deg}°): {round(cos_x,10):.10f}')

