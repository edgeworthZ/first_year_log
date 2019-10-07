text = 'F'+input('Toilet: ')+'F' #Add virtual empty rooms at each end
heavenRoom = list()
for i in range(1,len(text)-1):
    s = text
    if s[i] == 'B' or s[i-1] == 'B' or s[i+1] == 'B': continue
    s = s[:i]+'B'+s[i+1:]
    found = False
    for j in range(1,len(s)-1):
        if s[j-1:j+2] == 'FFF':
            found = True
            print(f'Cannot sit at room {i}, Found Space at room {j-1}-{j+1}')
    if not found:
        heavenRoom.append(i)
if len(heavenRoom) < 1:
    print('Walk back')
for room in heavenRoom:
    print(f'Room number {room}')
