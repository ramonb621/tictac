def game_board(board):
    # Update new instance of game board
    print("\n" * 100)

    '''
    OUTPUT: Current gameboard
    '''

    print(board[7]+"|"+board[8]+"|"+board[9])
    print("-----")
    print(board[4]+"|"+board[5]+"|"+board[6])
    print("-----")
    print(board[1]+"|"+board[2]+"|"+board[3])

test_board = ['#','X','O','X','O','X','O','X','O','X']
# game_board(test_board)

def player_input():

    marker = " "

    '''
    OUTPUT: Players input of two choices, 'X' or 'O'.
    '''

    while marker != "X" or marker != "O":
        input("Player 1: Select 'X' or 'O' as your marker to begin game.").upper()

        if marker == "X":
            return ("X", "O")
        else:
            return ("O", "X")


def place_marker(board, marker, position):
    board[position] = marker


# place_marker(test_board,'$', 9)
# game_board(test_board)

def check_win(board, mark):

    # Horizontal wins
    return ((board[7] == board[8] == board[9] == mark) or
    (board[4] == board[5] == board[6] == mark) or
    (board[1] == board[2] == board[3] == mark) or

    # Diagonal wins
    (board[7] == board[5] == board[3] == mark) or
    (board[9] == board[5] == board[1] == mark) or

    # Vertical Wins
    (board[7] == board[4] == board[1] == mark) or
    (board[8] == board[5] == board[2] == mark) or
    (board[9] == board[6] == board[3] == mark))


import random
def first_player():

    '''
    OUTPUT: Which player will go first
    '''
    
    if random.randint(0, 1) == 0:
        return "Player 2"
    else:
        return "Player 1"