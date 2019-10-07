def FormatThousand(s):
    res,s = str(),s[::-1]
    for i in range(len(s)):
        if i > 0 and i%3 == 0:
            res = ','+res
        res = s[i]+res
    return res

def IsSquareOfTwo(n):
    i = 1
    while(i <= n):
        i = i*2
        if i == n: return True
    return False

def Squarelize(w,l):
    if w < 1 or l < 1: return 0
    if w == 1 or l == 1: return w*l
    
    i = 2
    while(True):
        if w == l and IsSquareOfTwo(w) and IsSquareOfTwo(l):
            return 1
        if 2*i <= min(w,l):
            i *= 2
            continue
        else:
            break
    return Squarelize(i,i)+Squarelize(w-i,l)+Squarelize(l-i,i)

w = int(input('width: '))
l = int(input('ledgth: '))
if w > 0 and l > 0:
    print(f"Saito: It's {FormatThousand(str(Squarelize(w,l)))} estate(s).")
else:
    print('There is no estate here!')
