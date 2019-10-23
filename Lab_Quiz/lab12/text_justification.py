words = input('Words: ')
width = int(input('Max width: '))
wds = words.split()

line = ''
for w in wds:
    if len(line)+len(w) <= width:
        line = line+f'{w} '
    else: # print this line and create new line
        if line.count(' ') > 1:
            line = line[:len(line)-1] # Erase last space
        i = 0
        while(width-len(line) > 0):
            if line[i] == ' ' and line[i-1] != ' ': # is this the beginning of space(s)?
                line = line[:i]+' '+line[i:]
                i += 1
                if width-len(line) < 0:
                    break
            i =(i+1)%len(line) # iterate to next index with wrap around
        print(f'"{line}"')
        line = f'{w} '
else: # Last line
    while(width-len(line) > 0):
        line = line+' '
    print(f'"{line}"')
