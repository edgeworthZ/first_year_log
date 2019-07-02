rate = 25
minutes = int(input('Enter minutes: '))
hour = minutes/60 if (minutes%60 == 0) else minutes//60+1
fee = rate*hour
print(f'Parking fee is {int(fee)}')
