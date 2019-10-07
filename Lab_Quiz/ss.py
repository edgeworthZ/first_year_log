def globalVar():
    '''Could we have the global scope access?'''
    global eggs
    print(f'{globalVar.__name__}: eggs = {eggs}.')
    eggs = 5
    print(f'{globalVar.__name__}: eggs now = {eggs}.')
    
'''MAIN begins here'''
print('START')
eggs = 7
globalVar()
print(f'In MAIN, eggs = {eggs}.')
print('DONE')
