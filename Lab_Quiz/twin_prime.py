def isPrime(n):
    if n < 2:
        return False
    for i in range(2,n//2+1):
        if n%i == 0:
            return False
    return True

N = int(input('N: '))
while(True):
    if(isPrime(N) and isPrime(N+2)):
       break
    N += 1
print(f'({N},{N+2})')
