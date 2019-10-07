def isPrime(n):
    if(n < 2):
        return False
    res = True
    for i in range(2,n):
        if n%i == 0:
            res = False
            break
    return res

def hasCofactor(n):
    k = 1
    if isPrime(n):
        return k
    for i in range(2,n//2+1):
        if(n%i==0):
            k = i
            break
    return k

def myCoFactor(n):
    res = []
    if hasCofactor(n)==1:
        return res
    while hasCofactor(n) != 1:
        res.append(hasCofactor(n))
        n = n//hasCofactor(n)
    res.append(n)
    return res

def CountPrimeNDigit(n):
    nums = [x for x in range (10**(n-1),10**n)]
    primes = [n for n in nums if isPrime(n)]
    print('Count:',len(primes),'Result:',primes)

def MyFactor(n):
    nums = [x for x in range(1,n+1) if n%x == 0]
    return nums

a = myCoFactor(300)
print(a)
