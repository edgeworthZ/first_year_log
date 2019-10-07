class BaseNumber:
    def __init__(self,base,value):
        self.base = base
        self.value = value
        self.dec = self.GetDecimal()
        
    def GetDecimal(self):
        dec = 0
        digit = len(self.value)
        for i in range(0,digit,1):
            c = self.value[-1-i] if self.value[-1-i].isnumeric() else ord(self.value[-1-i])-55
            dec += int(c)*self.base**i
        return dec

    def ConvertToBase(self,base):
        res = ''
        tempDec = self.dec
        while(True):
            c = tempDec%base
            c = chr(c+55) if(c >= 10) else str(c)
            res = str(c)+res
            tempDec = tempDec//base
            if(tempDec == 0): break
        return res

def hex2bin(value):
    num = BaseNumber(16,value)
    return num.ConvertToBase(2)
    
def bin2hex(value):
    num = BaseNumber(2,value)
    return num.ConvertToBase(16)

def add_hex(x, y):
    x,y = BaseNumber(16,x),BaseNumber(16,y)
    z = BaseNumber(10,str(x.GetDecimal()+y.GetDecimal()))
    return z.ConvertToBase(16)

def main():
    val = input('(1-hex2bin). Try input a hexadecimal number: ')
    print(f"{' ':<12} Binary number of hexadecimal number {val} is {hex2bin(val)}")
    val = input('(2-bin2hex). Try input a binary number: ')
    print(f"{' ':<12} Hexadecimal number of binary number {val} is {bin2hex(val)}")
    val = input(f"{'(3-add_hex).':<12} Try input first hexadecimal number: ")
    val2 = input(f"{' ':<12} Try input second hexadecimal number: ")
    print(f"{' ':<12} Sum of hexadecimal numbers {val} and {val2} is {add_hex(val,val2)}")

main()
