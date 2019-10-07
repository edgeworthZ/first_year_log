prime=[2]

def cutLastDigit(number):
    return (number%10,number//10)

def cutFirstDigit(number):
    number = str(number)
    return (int(number[0]),int(number[1::1]))

def isPrime(number):
    if number in prime:
        return True
    if number < 2:
        return False
    for i in range(2,number):
        if number%i==0:
            return False
    prime.append(number)
    return True

inputnum = int(input("Positive Integer: "))

is_prime=isPrime(inputnum)
is_kodprime=True

other1=inputnum
other2=inputnum

for _ in range(len(str(inputnum))-1):
    first,other1 = cutFirstDigit(other1)
    is_kodprime&=isPrime(first)
    is_kodprime&=isPrime(other1)
    last,other2 = cutLastDigit(other2)
    is_kodprime&=isPrime(last)
    is_kodprime&=isPrime(other2)

is_kodprime&=is_prime

if is_prime:
    print(inputnum,"is Prime")
else:
    print(inputnum,"is not Prime")
if is_kodprime:
    print(inputnum,"is Kod Prime")
else:
    print(inputnum,"is not Kod Prime")
