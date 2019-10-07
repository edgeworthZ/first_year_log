d1 = input('DNA1: ')
d2 = input('DNA2: ')
if d1[0] != '3':
    d1 = d1[::-1]
if d2[0] != '5':
    d2 = d2[::-1]
d1 = d1[1:len(d1)-1]
d2 = d2[1:len(d2)-1]
comb = list(zip(d1,d2))
res = all(pair in [('A','T'),('T','A'),('C','G'),('G','C')] for pair in comb)
if res:
    print('Matched!')
else:
    print('Mismatched!')
