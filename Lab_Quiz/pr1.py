import time



n = int(input('Prime n: '))



start = time.time()





def isPrime(n, primes):

    for i in primes:

        if i > int(n**0.5)+1:

            break

        if n % i == 0:

            return False

    return True





prime_numbers = []



for i in range(2, n+1):

    if isPrime(i, prime_numbers):

        prime_numbers.append(i)

        print('Last found:', i)



total_time = time.time()-start



print('Time used: %.4f ms' % (total_time*1000))

# print(prime_numbers)

print('Sum Primes under', n, ':', sum(prime_numbers))
