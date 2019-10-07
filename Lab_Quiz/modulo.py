N = int(input('N: '))
M = int(input('M: '))
ls = list()
n = 1
while(n <= N):
    ls.append(int(input(f'Input Number {n}: ')))
    n += 1
mod_ls = list(map(lambda x:x%M,ls))
unique_mod = set(mod_ls)
print(len(unique_mod))
