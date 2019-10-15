text = input('Text: ')
text = [c for c in text.lower() if ord(c) in range(ord('a'),ord('z')+1)] # Format text
kw = input('Keyword: ')
kws = sorted(kw) # Sorted keyword
upTable = {}
for i in range(len(kw)):
    upTable[i+1] = kws[i]
#print(upTable)
lowTable = list()
i = 0
while(i < len(text)):
    row = ['x']*len(kw)
    for j in range(len(kw)):
        if not i < len(text): break
        row[j] = text[i]
        i += 1
    lowTable.append(row)
'''for t in lowTable:
      print(*t)'''
res = ''
for k in upTable.keys(): # Read by keywords' order
    #print(upTable[k])
    j = kw.index(upTable[k])
    for i in range(len(lowTable)):
        res = res + lowTable[i][j]
print('"{res}'')
