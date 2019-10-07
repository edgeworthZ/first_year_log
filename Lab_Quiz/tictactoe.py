from random import randint

def saito_bot_play(ox_map):
    i = randint(0,len(ox_map)-1)
    j = randint(0,len(ox_map)-1)
    while ox_map[i][j] != '-':
        i = randint(0,len(ox_map)-1)
        j = randint(0,len(ox_map)-1)
    return i,j

def CheckWinner(board):
    res = list()
    diag1,diag2 = list(),list()
    for i in range(len(board)): # Create a list of two Diagonals
        for j in range(len(board[0])):
            if i == j:
                diag1.append(board[i][j])
                diag2.append(board[i][::-1][j])
    res.append(diag1)
    res.append(diag2)
    
    for line in board+list(zip(*board)): # Create a list of rows and columns
        res.append(line)
        
    for line in res: # Check all
        if all([n == 'X' for n in line]): return 'You'
        if all([n == 'O' for n in line]): return 'Saito'

def PrintBoard(board):
    for row in board: print(*row)

size = int(input('Input size: '))
board = [['-' for col in range(size)] for row in range(size)]
player = input('Starting with? (O or X): ')
turn = 0
while(turn < size**2):
    if player == 'X': # Player's turn
        while(True): # Prevent player from overwriting existing mask
            i = int(input('Enter row: '))
            j = int(input('Enter column: '))
            if board[i][j] != '-':
                continue
            break
        board[i][j] = player
        player = 'O'
    else: # Bot's turn
        i,j = saito_bot_play(board)
        print(f'Saito choose ({i},{j})')
        board[i][j] = player
        player = 'X'
    PrintBoard(board)
    res = CheckWinner(board)
    if res:
        print('==========')
        print('Winner is',res)
        PrintBoard(board)
        break
    turn += 1
if turn >= size**2: # Loop ended without having a victor
    print('Draw')
