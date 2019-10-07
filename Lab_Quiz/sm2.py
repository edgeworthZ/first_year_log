def isPrime(n):
    if n < 2:
        return False
    for i in range(2,n+1//2):
        if n%i == 0:
            return False
    return True

n = int(input('Enter a number: '))
primes = [x for x in range(2,n) if isPrime(x)]
pairs = [[x,y] for x in primes for y in primes if x+y == n and x <= y]
print(len(pairs))
