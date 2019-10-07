sol = int(input('Enter Soldier(s): '))
work = int(input('Enter Work(s): '))
year = int(input('Enter Year(s): '))
kill = [] 
for i in range(year):
    kill.append(int(input('Enter Kill(s): ')))
solc = 0
workc = 0
y = 1
while(True):
    if y > year:
        break

    #start of year
    for i in range(sol):
        workc += 1
    for i in range(work):
        workc += 1
        solc +=1
    workc += 1

    #war
    if sol >= kill[y-1]:
        sol -= kill[y-1]
    elif sol+work >= kill[y-1]:
        work -= kill[y-1]-sol
        sol = 0
    elif sol+work+solc >= kill[y-1]:
        solc -= kill[y-1]-work-sol
        work,sol = 0,0
    elif sol+work+solc+workc >= kill[y-1]:
        workc -= kill[y-1]-work-sol-solc
        work,sol,solc = 0,0,0
    else:
        work,sol,solc,workc = 0,0,0,0

    #end of year, no adult survives
    sol,work = 0,0
        
    for i in range(solc):
        sol += 1
    for i in range(workc):
        work += 1
    solc, workc = 0,0
    
    y+=1
print(work)
print(sol)
