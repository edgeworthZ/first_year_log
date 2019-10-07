def findMax(nums):
    return max(nums)

def find2ndMax(nums):
    mxs = [x for x in nums if x != max(nums)]
    return max(mxs)

def sumEvenTerm(nums):
    return sum(filter(lambda x:x%2==0,nums))

def isPrime(n):
    if n < 2:
        return False
    for i in range(2,n):
        if n%i == 0:
            return False
    return True

def find2ndPrime(nums):
    found = False
    for i in range(len(nums)):
        if(isPrime(nums[i])):
            if(found):
                return nums[i]
            else:
                found = True

def isFibo(n):
    if(n < 0):
        return False
    if(n < 1):
        return True
    fb = [0,1,1]
    while(True):
        lastIndex = len(fb) -1
        if(n == fb[lastIndex]):
            return True
        else:
            if(n > fb[lastIndex]):
                fb.append(fb[lastIndex]+fb[lastIndex-1])
            elif(n < fb[lastIndex]):
                return False

def sumFibo(nums):
    return sum([x for x in nums if isFibo(x)])

def sumOddEvenTerm(nums):
    '''sum = 0
    for i in range(len(nums)):
        sum += nums[i]*(-1)**(i%2)
    return sum'''
    return sum([x*(-1)**(i%2) for i,x in enumerate(nums)])

def findUniqueItem(nums):
    '''unique = []
    tmp = nums[:]
    single = sorted(set(tmp),key=tmp.index)
    for n in single:
        tmp.remove(n)
        if n not in tmp:
            unique.append(n)
    return unique'''
    '''unique = []
    taboo = []
    for n in nums:
        if n in taboo:
            continue
        if n not in unique:
            unique.append(n)
        else:
            unique.remove(n)
            taboo.append(n)
    return unique'''
    return [x for x in nums if nums.count(x) == 1]

def mixStringNum(ls,n):
    return [c+str(i) for i in range(1,n+1) for c in ls ]

def myUnion(A,B):
    return list(set([x for x in A+B]))

def myIntersect(A,B):
    return [x for x in A if x in B]

def myMinus(A,B):
    return [x for x in A if x not in B]

A = [1, 2, 6, 7]
B = [1, 3, 4, 5, 8]
X = [1, 6, 9]
Y = [1, 3, 5, 6, 8, 9]
print(findMax([1,2,3,4,5,6]))
print(find2ndMax([1,2,3,4,5,6]))
print(sumEvenTerm([1,2,3,4,5,6]))
print(find2ndPrime([13,18,27,5,2,4,17,7,3]))
print(sumFibo([13,18,27,5,2,144,17,7,21,3]))
print(sumOddEvenTerm([1,2,3,4,5,6,7,-8,-9]))
print(findUniqueItem([13,18,27,5,21,144,17,27,21,13]))
print(mixStringNum(['p','q'],5))
print(myUnion(A,B))
print(myUnion(X,Y))
print(myIntersect(A,B))
print(myIntersect(X,Y))
print(myMinus(A,B))
print(myMinus(X,Y))
