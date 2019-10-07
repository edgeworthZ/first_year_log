def bin_search(item, items):
    if len(items) == 0:
        return False
    elif len(items) == 1:
        return items[0] == item
    mid_pos = len(items)//2 - 1
    mid_val = items[mid_pos]
    if item == mid_val:
        return True
    elif item > mid_val:
        return bin_search(item, items[mid_pos+1:])
    else:
        return bin_search(item, items[:mid_pos])

def find_std(name,names):
    res = bin_search(name,names)
    if res:
        res = names.index(name)
        return res+1
    else:
        return None

names = input('Enter list of students: ').split(' ')
names = sorted(names)
name = input('Enter student name: ')
std = find_std(name, names)
if std != None:
    print(f'{name} is STD{std:02}')
else:
    print(f'{name} is not found in list')
