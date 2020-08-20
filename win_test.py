from UnbeatableTicTacToe import get_winner

board1 = [['X', '*', 'X'],
          ['X', 'X', '*'],
          ['X', 'X', 'X']]
if get_winner(board1):
    print('ROW TEST PASSED')
else:
    print('ROW TEST FAILED')

board2 = [['X', '*', 'X'],
          ['O', '*', 'X'],
          ['X', '*', 'X']]

if get_winner(board2):
    print('COLUMN TEST PASSED')
else:
    print('COLUMN TEST FAILED')

board3 = [['X', '*', 'O'],
          ['O', 'O', 'X'],
          ['O', '*', 'X']]


if get_winner(board3):
    print('DIAGONAL TEST PASSED')
else:
    print('DIAGONAL TEST FAILED')

draw_board = [['X', 'X', 'O'],
              ['O', 'O', 'X'],
              ['X', 'O', 'X']]
if get_winner(draw_board) == False:
    print('DRAW TEST PASSED')
else:
    print('DRAW TEST FAILED')
