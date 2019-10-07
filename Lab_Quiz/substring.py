s = input('Text: ')
sub = input('Substring: ')
try:
    s.index(sub)
    res = s.replace(sub,f'[{sub}]')
    print(res)
except:
    print('Not found')
