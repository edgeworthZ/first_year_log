def decoration(ch,sp='#'):
    patterns = {1:['.','.',f'{sp}','.','.'],0:['.',f'{sp}','.',f'{sp}','.'],2:[f'{sp}','.',f'{ch}','.',f'{sp}']}
    for i in range(5):
        lines[i] = lines[i][:len(lines[i])-1] + patterns[(i+1)%2 + int((i+1)==3)] # Will show pat#3 at line 3

lines = [[],[],[],[],[]]
word = input('Word: ')
for i,c in enumerate(word):
    if (i+1)%3 == 0: decoration(c,'*')
    else: decoration(c)

for row in lines:
    for col in row:
        print(col,end='')
    print()
