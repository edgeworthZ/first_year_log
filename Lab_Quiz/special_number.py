def IsSpecialNumber(n):
    s = str(n)
    sum,pow = 0,0
    for c in s:
        pow += 1
        sum += int(c)**pow
    if(sum == n):
        return 'Y'
    else:
        return 'N'

ls = list()
while(True):
    n = int(input('Input: '))
    if(n == 0): break
    ls.append(n)
for n in ls:
    print(f'{IsSpecialNumber(n)}',end="")
print()
