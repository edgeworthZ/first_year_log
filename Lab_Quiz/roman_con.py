def FormatThousand(s):
    res,s = str(),s[::-1]
    for i in range(len(s)):
        if i > 0 and i%3 == 0:
            res = ','+res
        res = s[i]+res
    return res

def roman_con(s):
    dic = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
    res = 0
    for i in range(len(s)):
        if i > 0 and dic[s[i]] > dic[s[i - 1]]:
            res += dic[s[i]] - 2*dic[s[i - 1]]
        else:
            res += dic[s[i]]
    return str(res)

s = input('Roman number: ')
print(f'Arabic number is {FormatThousand(roman_con(s))}')
