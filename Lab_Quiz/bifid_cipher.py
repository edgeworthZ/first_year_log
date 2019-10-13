text = input('Text : ').upper()
dic = {}
cId = ord('A')
for i in range(1,6): # This loop generates first table
    for j in range(1,6):
        dic[chr(cId)] = str(i)+str(j)
        if chr(cId) == 'I':
            cId += 1
            dic[chr(cId)] = str(i)+str(j)
        cId += 1
table = list()
for i in range(len(text)): # This loop generates second table
    if ord(text[i]) in range(ord('A'),ord('Z')+1):
        table.append(dic[text[i]])
table = list(zip(*table)) # Transpose
table = table[0]+table[1] # Merge column to row
res = ''
for i in range(0,len(table),2): # Read each set of 2 characters
    bfId = table[i]+table[i+1]
    for key,val in dic.items(): # Search for key with interested value
        if val == bfId:
            res = res + key.lower()
if 'ij' in res:
    print(res.replace('j',''))
    print(res.replace('i',''))
else:
    print(res)
