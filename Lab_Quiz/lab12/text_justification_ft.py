#words = input('Words: ')
words = 'This is an example of text justification.'
w = words.split()
#print(w)
#max_width = int(input('Max width: '))
max_width = 16
s,res,i,count='',[],0,0
while True:
  s = s + w[i] + ' '
  i+=1
  if len(s)+len(w[i])-1>=max_width:
    s=s[:len(s)-1]
    ss = s.split()
    print(f'ss = {ss}')
    line = '' # this will be added to res after adding spaces
    count = 0 # total characters of words stored in ss
    for word in ss:
        count += len(word)
    while count<max_width-len(line): # repeat until count reaches max_width
        for j in range(len(ss)):
            if j < len(ss)-1 or j == 0: # j == 0 will always happen, in case of ss contains only one word
                ss[j] = ss[j]+' '
                count+=1
            if count==max_width:
                break
    for word in ss: # finished adding spaces, create a line from those words
        line += word
    res.append(line) # add the line to res for printing at the end
    print(f'res = {res}')
    s=''
  if i>len(w)-2: # last line?
    res.append(s+w[len(w)-1])
    while len(res[len(res)-1])<max_width:
        res[len(res)-1]+=' '
        if len(res[len(res)-1])==max_width:
            break
    break
for nl in res: print(f'{nl}(Length: {len(nl)})')
