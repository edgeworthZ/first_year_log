def paren_chk(s): #Recursive Attemp
    sp,spr = ['(','[','{'],[')',']','}']
    i = 0
    while(i < len(s)):
        if s[i] in spr:
            return False
        if s[i] in sp:
            found = True
            spi = sp.index(s[i])
            try:
                endSp = i
                while(True):
                    newEnd = s[endSp+1:].find(spr[spi])
                    if newEnd < 0: break
                    else: endSp = len(s[:endSp+1])+ newEnd 
                    if s[i] in s[i+1:endSp+1]: continue
                    else: break
            except:
                return False
            inside = s[i+1:endSp]
            #print('inside',s[i+1:endSp])
            outside = s[endSp+1:]
            #print('outside',s[endSp+1:])
            return paren_chk(inside) and paren_chk(outside)
            i = 0
        i += 1
    return True

s = input()
if paren_chk(s):
    print('Matched!')
else:
    print('Mismatched!')
