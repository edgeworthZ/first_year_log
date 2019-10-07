inputnum = int(input("Positive Integer: "))

prime = [inputnum]
startwith = 2

index=0
while True:
    for i in range(startwith,prime[index]+1):
        if prime[index]%i==0:
            if prime[index]//i != 1:
                prime.append(prime[index]//i)
            prime[index]=i
            startwith=i
            break
    index+=1
    if index>=len(prime):
        break

print(inputnum,": ",end='')
for i in prime:
    print(i,end=' ')
print()
