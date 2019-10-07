import math

mean = None
sd = None

def find_mean(*args):
    summ = 0
    n = len(args)
    global mean
    for i in range(0,n):
        summ += args[i]
    mean = summ/n
    return mean

def find_sd(*args):
    summ = 0
    n = len(args)
    global sd
    mean = find_mean(*args)
    for i in range(0,n):
        summ += (args[i] - mean)**2
    sd = math.sqrt(summ/n)
    return sd

variables = [float(input(f'Input number{x}: ')) for x in range(1,6)]
find_mean(*variables)
find_sd(*variables)
print(f'mean: {mean:.3f}')
print(f'sd: {sd:.3f}')
