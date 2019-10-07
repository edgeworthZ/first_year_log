import re

def calculate(s):
    print(s)

def factorial(x):
    res = 1
    for i in range(1,x+1):
        res *= i
    return res

s = input('Text: ')
dic = {}
for c in s:
    if c in dic: dic[c] += 1
    else:dic[c] = 1
price = 0.0
for key,val in dic.items():
    if re.match(r"[A-Z]", key): tx,c = 890,4
    elif re.match(r"[a-z]", key): tx,c = 615,3
    elif re.match(r"[0-9]", key): tx,c = 150,7
    else: tx,c = 100,3
    price += tx * (val//c)
    rem = val%c
    for i in range(1,rem+1):
        price += factorial(i+1)/(10-i)
print(f'Price: {price:.2f}')
