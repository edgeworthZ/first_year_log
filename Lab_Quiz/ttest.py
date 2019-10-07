import time

def isPrime(n):
    if n < 2:
        return False
    for i in range(2,n//2+1):
        if n%i == 0:
            return False
    return True

def isFibo(n):
    if n < 0:
        return False
    if n < 2:
        return True
    fibo = [0,1,1]
    while(True):
        lastIndex = len(fibo)-1
        if fibo[lastIndex] > n:
            return False
        elif fibo[lastIndex] == n:
            return True
        else:
            fibo.append(fibo[lastIndex]+fibo[lastIndex-1])

def Q1(n=1000):
    primes = [x for x in range(1,n) if isPrime(x)]
    fibos = [x for x in range(1,n) if isFibo(x)]
    return primes,fibos

def isPrime2(n):
  if n<2:
    return False
  res = True
  for i in range(2,n//2+1):
    if n%i==0:
      res = False
      break
  return res

def isFibo2(n):
  if n<1:
    return False
  if n==1:
    return True
  t1,t2,newt = 1,1,0
  while newt < n:
    newt = t1+t2
    if newt == n:
      return True
    t1,t2 = t2,newt
  return False
  
def Q12():
  plist,flist = [],[]
  for i in range(1000):
    if isPrime2(i):
      plist.append(i)
    if isFibo2(i):
      flist.append(i)
  return plist,flist

starttime = time.time()
print('Q1:',Q1())
totaltime = time.time()-starttime
print('Time used: %.4f ms' % (totaltime*1000))
