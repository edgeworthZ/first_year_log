'''def Bin2GrayZipVersion(n):
    return [str(sum(val)%2) for val in zip(bn,[0]+bn[:len(bn)])]'''

def Bin2Gray(bn):
    bn = int(bn,2)
    bn ^= (bn >> 1) # Shift to right 1 time and XOR with previous value
    return bin(bn)[2:]

def Gray2Bin(bn):
    bn = int(bn,2) # convert to int
    mask = bn
    while mask != 0:
        mask >>= 1 # Shift to right and assign it
        bn ^= mask # XOR
    return bin(bn)[2:]

dec = int(input('Input Decimal: '))
grc = input('Input Gray Code: ')
bn = bin(dec)[2:]
res = Bin2Gray(bn)
if int(grc) == int(res):
    print(True)
else:
    print(f'False, Fixed Decimal is {int(Gray2Bin(grc),2)}')
