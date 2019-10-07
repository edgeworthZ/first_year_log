def IsConnect(w1,w2):
    res = [a == b for a,b in zip(w1,w2)]
    for i in range(len(res)-2):
        if(res[i] == res[i+1] == False and res[i+2] != True):
            return False
    return True

s = [w for w in input('Text: ').split()]
disconPoints,chainsLength = list(),list()
entryLength = 1
for i in range(len(s)-1):
    if IsConnect(s[i],s[i+1]):
        entryLength += 1
    else:
        disconPoints.append(i)
        chainsLength.append(entryLength)
        entryLength = 1
else:
    chainsLength.append(entryLength)
amount_chain = len(disconPoints)+1
longest_chain = max(chainsLength)
print(f'{amount_chain} Chain(s). Maximum length is {longest_chain} word(s).')
