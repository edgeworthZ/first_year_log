def d2h(d):
    '''Convert dec value to hex characters, eg. 12 -> "C"'''
    h = ''
    if d==10:
        h = 'A'
    elif d == 11:
        h = 'B'
    elif d == 12:
        h = 'C'
    elif d == 13:
        h = 'D'
    elif d == 14:
        h = 'E'
    elif d == 15:
        h = 'F'
    else:
        h = str(d)
    return h

def dec2hex(dec):
    hex = ''
    while dec > 0:
        hex = d2h(dec%16) + hex
        dec = dec//16
    return hex

def dec2oct(dec):
    oct = ''
    while dec > 0:
        oct = d2h(dec%8) + oct
        dec = dec//8
    return oct

#-- You can debug the above functions by decommenting the lines below
print(dec2hex(123456)) # 1E240
print(dec2oct(123456)) # 361100

def main1():
    print(f"{'n':^5}", '\t', f"{'2**n':^5}", '\t', f"{'b8':^5}", '\t', f"{'b16':^5}")     #table column headings
    print("-"*5, '\t', "-"*5, '\t', "-"*5, '\t', "-"*5)
    for x in range(13):        # generate values for columns
        print(f"{x:^5}", '\t', f"{2**x:>5}", '\t', f"{dec2oct(2**x):>5}", '\t', f"{dec2hex(2**x):>5}")

#-- You can debug the above main1() function by decommenting the lines below
main1()

def dec2bin(dec):
    bin = ''
    while dec > 0:
        bin = str(dec%2) + bin
        dec = dec//2
    return bin

#-- You can debug the above main1() function by decommenting the lines below
print(dec2bin(123456)) # 11110001001000000

def hex2bin(hex):

### Your homework today (i.e., 13AUG2019)
# You need to implement and test the following functions
# hex2bin() : Convert a string that represents hexadecimal to binary number
# bin2hex() : Convert a string that represents binary number to hexadecimal
# add_hex(x, y) : Calculate the result from adding two hexadecimal numbers, i.e. the input parameters x and y, the result should be a hexadecimal number.
#
# hint: well study these lines of codes, they will be very helpful to complete this homework
s = "AFD890"
print(s)
for i in range(len(s)):
  print(f's[{i}]: {s[i]}')
### ----------------------------------------------------------------------------------

