s = input('Text: ')
sub = input('Substring: ')
i = 0
res = s
try:
    s.index(sub)
    res = s.replace(sub,f'[{sub}]')
except:
    while(True):
        if i+len(sub) > len(res):
            break
        error,erP = 0,0
        for j in range(len(sub)):
            if res[i+j] != sub[j]:
                error += 1
                erP = j
        if error > 1:
            i+= 1
        else:
            if error == 1:
                _sub = sub[:erP]+'?'+sub[erP+1:]
            else:
                _sub = sub
            res = res[:i]+'['+_sub+']'+res[i+len(_sub):]
            i+= len(_sub)+2
print(res)
