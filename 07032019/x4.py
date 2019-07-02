import math

rate = 25
minutes = int(input('Enter minutes: '))
hour = math.ceil(minutes/60)
fee = rate*hour
print(f'Parking fee is {fee}')
