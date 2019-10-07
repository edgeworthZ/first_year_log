def isPrime(n):
    if n < 2:
        return False
    for i in range(2,n):
        if n%i == 0:
            return False
    return True

def isFibo(n):
    if n < 0:
        return False
    if n < 2:
        return True
    fibo = [0,1,1]
    while(True):
        lastIndex = len(fibo)-1
        if fibo[lastIndex] > n:
            return False
        elif fibo[lastIndex] == n:
            return True
        else:
            fibo.append(fibo[lastIndex]+fibo[lastIndex-1])

def SelectionSort(ls):
    for i in range(len(ls)):
        minPos = i
        for j in range(i,len(ls)):
            if ls[j] < ls[minPos]:
                minPos = j
        ls[minPos],ls[i] = ls[i],ls[minPos]
    return ls

def InsertionSort(ls):
    if len(ls) < 2:
        return ls
    for i in range(1,len(ls)):
        val = ls[i]
        for j in range(i-1,-1,-1):
            if ls[j] > val:
                ls[j+1] = ls[j]
            else:
                ls[j+1] = val
                break
    return ls

def isPalindrome(n):
    if str(n) == str(n)[::-1]:
        return True
    return False

def isLeapYear(y):
    if y%4 == 0 and (y%100 != 0 or y%400 == 0):
        return True
    return False

def CountDays(d,m,y):
    monthdays = [31,28,31,30,31,30,31,31,30,31,30,31]
    dtotal = 0
    dtotal += d
    for i in range(1,m):
        if(i == 2 and isLeapYear(y)):
            dtotal += 1
        dtotal += monthdays[i-1]
    for i in range(1,y):
        if isLeapYear(i):
            dtotal += 366
        else:
            dtotal += 365
    return dtotal

def Q1(n=1000):
    primes = [x for x in range(1,n) if isPrime(x)]
    fibos = [x for x in range(1,n) if isFibo(x)]
    return primes,fibos

def Q2(ls=[1,5,4,'Hello',4.0,6.3,'x',1,5.6]):
    ints = [val for val in ls if type(val) is int]
    strings = [val for val in ls if type(val) is str]
    floats = [val for val in ls if type(val) is float]
    return ints, strings, floats

def Q3(ls=[1,7,11,13,5,2,4,6,2,1,9,16],mode='Insertion'):
    if mode.lower() == 'selection':
        return SelectionSort(ls)
    elif mode.lower() == 'insertion':
        return InsertionSort(ls)

def Q4(n=8):
    cubes = [x**3 for x in range(1,n)]
    return sum(cubes)

def Q5(ls=[1,2,5]):
    pairs = [[u,v] for u in ls
             for v in ls if u != v and u < v]
    return sum([x[1]-x[0] for x in pairs])

def Q6(ls=[48,1024]):
    comdivs = [x for x in range(1,min(ls)+1)
               if all([val%x == 0 for val in ls])]
    return comdivs

def Q7(n=1473):
    while(True):
        if(isPalindrome(n)):
           break
        r = int(str(n)[::-1])
        n = n+r
    return n

def Q8(*args):
    args = list(args)
    i,carry = 0,0
    while(True):
        if i >= len(args)-1:
            break;
        n1, n2 = str(args[i]),str(args[i+1])
        pads = abs(max(len(n1),len(n2)))
        n1,n2 = f'{n1:>0{pads}}',f'{n2:>0{pads}}'
        sm = [int(x[0])+int(x[1]) for x in zip(n1,n2)]
        for j in reversed(range(len(sm))):
            if sm[j] // 10 > 0:
                sm[j-1] += j%10
                carry += 1
        args[i+1] = args[i]+args[i+1]
        i+=1
    return carry

def Q9(s='25,35,15,16,30,45,37,39'):
    ls = [int(x) for x in s.split(',')]
    ls = sorted(ls)[::-1]
    return f'{ls[0]},{ls[1]},{ls[2]}'

def Q10(dmy='1246/2/28'):
    date = ['Friday','Saturday','Sunday','Monday','Tuesday','Wednesday','Thursday']
    months = ['January','February','March','April','May','June',
              'July','August','September','October','November','December']
    y,m,d = [int(x) for x in dmy.split('/')]
    friday = CountDays(1,1,2016)%7
    today = CountDays(d,m,y)%7
    return f'{d} {months[m-1]} {y} is {date[today-friday]}.'

def Q11(s="Thank you for your comment and your participation. I love the comment so much."):
    words = s.lower().replace('.','').split()
    uni_words = set(words)
    freq = 0
    member = list()
    for w in uni_words:
        if words.count(w) > freq:
            member = list()
            freq = words.count(w)
            member.append(w)
        elif words.count(w) == freq:
            member.append(w)
    res = f'Most frequent words are: '
    for w in member:
        res += f'{w}({freq}) ,'
    return res[:len(res)-1]

print('Q1:',Q1())
print()
print('Q2:',Q2())
print()
print('Q3:',Q3())
print()
print('Q4:',Q4())
print()
print('Q5:',Q5())
print()
print('Q6:',Q6())
print()
print('Q7:',Q7())
print()
print('Q8:',Q8(786,457))
print()
print('Q9:',Q9())
print()
print('Q10:',Q10())
print()
print('Q11:',Q11())
print()
