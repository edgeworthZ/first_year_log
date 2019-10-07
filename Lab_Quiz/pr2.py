import time



n = int(input('Prime n: '))



start = time.time()



primes = [True]*(n+1)

prime_numbers = []



primes[0] = False

primes[1] = False



for i in range(n+1):

    if primes[i]:

        prime_numbers.append(i)

        print('Last Found:', i)

        for j in range(i*2, n+1, i):

            primes[j] = False



total_time = time.time()-start



print('Time used: %.4f ms' % (total_time*1000))

# print(prime_numbers)

print('Sum Primes under', n, ':', sum(prime_numbers))
