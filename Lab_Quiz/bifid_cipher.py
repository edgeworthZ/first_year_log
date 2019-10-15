text = input('Text : ').upper()
dic = {}
cId = ord('A')

def ToIJ(s,idx=0): # i/j  text
    if 'i' in s or 'j' in s:
        for i in range(idx,len(s)):
            if s[i] == 'i' or s[i] == 'j':
                iText,jText = s[:i]+'i'+s[i+1:],s[:i]+'j'+s[i+1:]
                allres.add(iText)
                allres.add(jText)
                ToIJ(iText,i+1)
                ToIJ(jText,i+1)
                break
    else: allres.add(s)

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
            res = res + key.lower() # i/j will come in pair
allres = set()
ToIJ(res.replace('ij','j')) # Get all variations of i/j
for t in allres: print(f'"{t}"')
