def typeWriting(order):
    step = 0
    startIndex = 0
    txt = ''
    for i in range(len(order)):
        for ii in range(startIndex,len(order[i])):
            txt = txt + order[i][ii]
            step += 1
            #print(txt,step)
        step += 1 # Print
        #print(txt,step)
        if i == len(order)-1: break # Done
        startIndex = len(txt)
        while(True):
            txt = txt[:len(txt)-1]
            startIndex -= 1
            step += 1
            #print(txt,step)
            #print(txt,order[i+1][:startIndex])
            if txt == order[i+1][:startIndex] or len(txt) < 1:
                break
    return step

from itertools import permutations

n = int(input('N: '))
txts = []
for i in range(n):
    txts.append(input())
#shortest = min(txts,key=len)

orders = list(permutations(txts, len(txts)))
steps = list()
for order in orders:
    steps.append(typeWriting(order))
print(min(steps))
