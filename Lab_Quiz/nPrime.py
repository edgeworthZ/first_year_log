n = int(input('n: '))

number_range = [True for _ in range(10**n)]
count=0

for number in range(10**n):
    #Isn't Prime or less than 2
    if number_range[number]==False or number < 2:
        number_range[number]=False
        continue
    #Number we want
    if number>=(1+10**(n-1)):
        count+=1
    #Check for not prime
    for not_prime in range(number*2,10**n,number):
        number_range[not_prime]=False

print(count)
