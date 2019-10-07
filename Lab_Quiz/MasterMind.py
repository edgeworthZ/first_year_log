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

target = int(input('Enter a target (4-digit integer): ' ))
guess = int(input('Enter your guess (4-digit integer): ' ))

#Without using string or list's operation
correct_pos = []
correct_digits = []
_target = target
_guess = guess
for i in range(4):
    target1 = _target % 10
    guess1 = _guess % 10
    if(target1 == guess1):
        correct_pos.append(target1)
    elif(guess1 == target%10 or guess1 == target//10%10 or guess1 == target//100%10 or guess1 == target//1000%10):
        correct_digits.append(guess1)
    _target = _target//10
    _guess = _guess//10

if(len(correct_pos) > 3):
        print('Contratulations, you just mastered master mind!!')
else:
    str_pos = TextFormat(len(correct_pos),'position')
    str_digit =  TextFormat(len(correct_digits),'digit')
    print(f'{str_pos.capitalize()}, {str_digit}')
