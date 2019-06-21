#Nutawut Naprom
#Python

str1 = input('Enter your first text: ')
str2 = input('Enter your second text: ')

for i in range(0,len(str1),1):
    for j in range(i+1):
        common = str1[j:len(str1)-i+j]
        if(fString in str2):
            print('Longest sharing string is',fString)
            break
    else:
        continue
    break
