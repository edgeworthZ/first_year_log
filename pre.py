#Name: Nutawut Naprom
#Lang: Python

height = int(input('Enter your height: '))
discount = ''

if(height <= 120):
    discount = 'Free'
elif(height < 150):
    discount = str((150-height)*8)
elif(height < 164):
    discount = str((164-height)*3)
    
print(discount)
