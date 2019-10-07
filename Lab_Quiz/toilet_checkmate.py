text = input('Toilet: ')
found = False
tt = text.split('B')
target = list()
oIndex = 0
for i in range(len(tt)):
    if tt[i].count('F') == 3:
        found = True
        target.append(oIndex+2)
        target.append(oIndex+3)
    if tt[i].count('F') == 4:
        found = True
        if i+1 != len(tt):
            target.append(oIndex+2)
        target.append(oIndex+3)
    if i < len(tt)-1:
        if 'F' in tt[i] and 'F' in tt[i+1]:
            oIndex += 1
    oIndex += 1
if not found:
    print('Walk back')
else:
    for i in target:
        print(f'Room number {i}')
