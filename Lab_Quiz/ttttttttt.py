print('aBCDefG' > 'abC') --> False
print('3' < 5) --> Error
print(4//5*5%2) --> 0
print(math.ceil(3.14+2.00**2)+2//2) --> 9
print(-2**-2) --> -0.25
print(math.floor(-1/--10)) --> -1
print(math.log10(99+True**(False//True))) --> 2.0
print(bool(1) and bool(-1)) --> True
print(1 and 2) --> 2
print(1 or 0) --> 1
print(1 and 2 or 3) --> 2
print(not 2) --> False
print(not 0) --> True
print(False and -1) --> False
print(-1 or True) --> -1
print(-5 > False) --> False
print(0 == True) --> False
print(True or 0) --> True
print(not 1 and not 0 or -1) --> -1
print(35**False) --> 1
print(-3%7+3%7) -- > 7
print(not "" and not 1-True) --> True
print(abs(-1)+math.fabs(-2)) --> 3.0
print(math.factorial(1)+math.ceil(2.5)+math.floor(3.5)) --> 7


#61.Which statement causes an error?
print(f"""""Python 'is' Great""""")
print(""""{'''Py'''}"t"h"on 'is' Grea"'t:{.f}""""")
print(f""f'P'"y""""thon is"""' ''Gr'"eat")
#print('{{P}'"y"f'''Thon''{'I'}s Great}"''')
print(f'P''y'f't'"h"'o'"n"f"""{" 'is' "}"""'G'"r"''"eat")

