from UnbeatableTicTacToe import get_winner

board1 = [['X', '*', 'X'],
          ['X', 'X', '*'],
          ['X', 'X', 'X']]
if get_winner(board1) == 'QUIT':
    print('ROW TEST PASSED')
else:
    print('ROW TEST FAILED')

board2 = [['X', '*', 'X'],
          ['O', '*', 'X'],
          ['X', '*', 'X']]

if get_winner(board2) == 'QUIT':
    print('COLUMN TEST PASSED')
else:
    print('COLUMN TEST FAILED')

board3 = [['X', '*', 'O'],
          ['O', 'O', 'X'],
          ['O', '*', 'X']]


if get_winner(board3) == 'QUIT':
    print('DIAGONAL TEST PASSED')
else:
    print('DIAGONAL TEST FAILED')

draw_board = [['X', 'X', 'O'],
              ['O', 'O', 'X'],
              ['X', 'O', 'X']]
if get_winner(draw_board) == 'QUIT':
    print('DRAW TEST PASSED')
else:
    print('DRAW TEST FAILED')
