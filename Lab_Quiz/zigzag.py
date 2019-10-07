s = list(input('Input sentence: '))
rn = int(input('Input row: '))
i,res = 0,[]
while(True):
    if i > len(s)-1:
        break
    if i%(rn-1) == 0:
        row = s[i:i+rn]
        row = row + [None]*(rn-len(row))
        res.append(row)
        i += rn
    else:
        tem = [None]*rn
        tem[rn-1-(i%(rn-1))] = s[i]
        res.append(tem)
        i += 1
[[print(col,end='') for col in row if col] for row in zip(*res)]
        
