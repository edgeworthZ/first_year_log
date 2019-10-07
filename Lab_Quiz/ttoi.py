def check():
    for i in range(len(res)):
        if i>len(res)-2:
            break
        if res[i] == 'B':
            continue
        elif res[i] == 'F':
            if res[i-1] == 'F' and res[i+1] == 'F':
                r.append(i)
    return r

t = input('Toilet: ')
r = []
res = ['F']
for i in t:
    res.append(i)
res.append('F')
print(res)
print(check())
