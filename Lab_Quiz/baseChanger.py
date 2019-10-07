def ConvertToDecimal(base,baseValue):
    dec = 0
    digit = len(baseValue)
    for i in range(0,digit,1):
        c = baseValue[-1-i] if baseValue[-1-i].isnumeric() else ord(baseValue[-1-i])-55
        dec += int(c)*base**i
    return dec

def DecimalToNBase(base,baseValue):
    out = ''
    while(True):
        c = baseValue%base
        c = chr(c+55) if(c >= 10) else str(c)
        out = str(c)+out
        baseValue = baseValue//base
        if(baseValue == 0): break
    return out

def hex2bin(value):
    dec = ConvertToDecimal(16,value)
    return DecimalToNBase(2,dec)
    
def bin2hex(value):
    dec = ConvertToDecimal(2,value)
    return DecimalToNBase(16,dec)

def add_hex(x, y):
    res_dec = ConvertToDecimal(16,x)+ConvertToDecimal(16,y)
    return DecimalToNBase(16,res_dec)

val = input('(1-hex2bin). Try input a hexadecimal number: ')
print(f"Binary number of {val} is {hex2bin(val)}")
val = input('(2-bin2hex). Try input a binary number: ')
print(f"Hexadecimal number of {val} is {bin2hex(val)}")
val = input(f"{'(3-add_hex).':<12} Try input first hexadecimal number: ")
val2 = input(f"{' ':<12} Try input second hexadecimal number: ")
print(f"add_hex : {add_hex(val,val2)}")
