def isPrime(n):
    if n < 2:
        return False
    for i in range(2,n):
        if n%i == 0:
            return False
    return True

n = int(input('Input n: '))
prime = []
i = 2
sum = 0
while(True):
    if(isPrime(i)):
        prime.append(i)
    if(prime[len(prime)-1] >= n and (len(prime)-1)%2 == 0):
        break
    i+=1
for j in range(len(prime)):
    if j%2 ==0:
        print('odd',prime[j])
    else:
        print('even',prime[j])
for i in range(len(prime)):
    if i%2 == 0:
        sum += prime[i]
print(sum)
