def TextFormat(n, vType):
    str_pos = None
    if(n > 2):
        str_pos = 'three '+ vType + 's'+ ' correct'
    elif(n > 1):
        str_pos = 'two '+ vType + 's'+ ' correct'
    elif(n > 0):
        str_pos = 'one '+ vType + ' correct'
    else:
        str_pos = 'no '+ vType + 's'+ ' correct'
    return str_pos

target = input('Enter a targetget (4-digit integer):' )
guess = input('Enter your guessss (4-digit integer):' )

correct_pos = [target[i] for i in range(4) if target[i]==guess[i]]
correct_digits = [digit for digit in target if (digit in guess and digit not in correct_pos)]

if(len(correct_pos) > 3):
        print('Contratulations, you just mastered master mind!!')
else:
    str_pos = TextFormat(len(correct_pos),'position')
    str_digit =  TextFormat(len(correct_digits),'digit')
    print(f'{str_pos.capitalize()}, {str_digit}')
