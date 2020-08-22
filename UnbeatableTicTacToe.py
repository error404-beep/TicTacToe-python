# import game_client
# import game_server

def new_board():
    board = [['*' for _ in range(3)] for _ in range(3)]
    return board


def render_board(board):
    print('_' * 20)
    print('  | 0 | 1 | 2 | ')
    print('_' * 20)
    for i in range(3):
        print(f'{i} |', end=' ')
        for j in range(3):
            print(board[i][j], end=' | ')
        print()
        print('_' * 20)


def take_input(player):
    print(f'Turn: {player}')
    try:
        y = int(input("Pls enter the X co-ordinate of your move:\t"))
        x = int(input("Pls enter the Y co-ordinate of your move:\t"))
    except ValueError:
        print('Input Value Wrong')
        return take_input(player)
    return x, y


def make_move(board, player, move):
    new_board = board
    new_board[move[0]][move[1]] = player
    return new_board


def validate_move(move, board):

    if (move[0] > 2 or move[0] < 0 or move[1] > 2 or move[1] < 0):
        print("Invalid Input. Please enter only values from 0 to 2")
        return True
    corr_box = board[move[0]][move[1]]
    if corr_box == '*':
        return False  # Stops the while loop for turn
    else:
        return print(f"Invalid position. Position already occupied by {corr_box}")


def get_winner(board):
    draw = True
    for i in range(3):
        for j in range(3):
            if board[i][j] == '*':
                draw = False
    if draw:
        print('OH NO! IT\'S A DRAW')
        return 'QUIT'
    # Check for rows:
    for row in board:
        if (not '*' in row) and (row[0] == row[1] == row[2]):
            print(f'CONGRATULATIONS {row[0]} HAS WON THE GAME. ROW')
            return 'QUIT'

    # Checks for columns
    for j in range(3):
        if (board[0][j] == board[1][j] == board[2][j]) and board[0][j] != '*':
            print(f'CONGRATULATIONS {board[0][j]} HAS WON THE GAME. COLUMN')
            return 'QUIT'
    # CHecks for diagonals:
    if ((board[0][0] == board[1][1] == board[2][2]) or (board[0][2] == board[1][1] == board[2][0])) and board[1][1] != '*':
        print(f'CONGRATULATIONS {board[1][1]} HAS WON THE GAME. DIAGNOL')
        return 'QUIT'
    
    return False


def runner_code(board):
    turn = 1
    # render_board(board)
    while get_winner(board) != 'QUIT':
        if turn == 1:
            player = 'X'
        else:
            player = 'O'

        # Move input and validation
        val = True
        while val:
            move = tuple(take_input(player=player))
            if validate_move(move, board):
                val = True
            else:
                val = False

        board = make_move(board, player, move)
        render_board(board)
        # Alternate Turn
        print(f'Earlier turn {turn}')
        if turn == 1:
            turn = 0
        elif turn == 0:
            turn = 1
        print(f'After turn {turn}')

    


if __name__ == "__main__":
    board = new_board()
    render_board(board)

    runner_code(board)

# board = new_board()
# render_board(board)
# # move = tuple(take_input())
# print(move)
# new_board = make_move(board, 'X', move)
# new_board = make_move(board, 'O', move)
# print('New Board')
# render_board(new_board)
