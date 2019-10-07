def fac(n):
    if n < 2:
        return 1
    return n*fac(n-1)

def FormatThousand(s):
    res,s = str(),s[::-1]
    for i in range(len(s)):
        if i > 0 and i%3 == 0:
            res = ','+res
        res = s[i]+res
    return res

n = int(input('n: '))
if -1 < n < 101:
    res = str(fac(n))
    print(f'Factorial of {n} is {FormatThousand(res)}.')
else:
    print(f'{n} is not an integer in range [0,100]')
