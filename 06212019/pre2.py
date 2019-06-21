#Name: Nutawut Naprom
#Lang: Python

cuttableChar = input('Enter a character you want to cut: ')
text = input('Enter your text: ')
        
sectionList = text.split(cuttableChar)
cutCount = len(sectionList)-1
legitSections = [sec for sec in sectionList if len(sec)>0]

print(cutCount)
print(len(legitSections))
