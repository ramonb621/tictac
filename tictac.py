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

# test_board = ['#','X','O','X','O','X','O','X','O','X']
# game_board(test_board)

def player_input():

    marker = ""

    '''
    OUTPUT: Players input of two choices, 'X' or 'O'.
    '''

    while marker != "X" or marker != "O":
        marker = input("Player 1: Select 'X' or 'O' as your marker to begin game.").upper()

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

def space_check(board, position):
    return board[position] == " "

def board_check(board):

    '''
    OUTPUT: If game board full, will return 'True' else 'False'
    '''

    for i in range(1, 10):
        if space_check(board, i):
            return False
    return True

def player_choice(board):

    position = 0

    while position not in [1, 2, 3, 4, 5, 6, 7, 8, 9] or not space_check(board, position):
        try:
            position = int(input("Enter your next position: (1-9) "))
        except:
            print("Pick again.")
    return position

def replay():

    # enter = " "

    # while enter != "Y" or enter != "N":
    #     input("Do you want to play again? Enter 'Y' for 'Yes' or 'N' for 'No.'").upper()
    #     if enter == "Y":
    #         return True
    #     else:
    #         return False
    return input("Do you want to play again? Enter 'Y' for 'Yes' or 'N' for 'No.'").upper().startswith("y")

# PLAY GAME

print("Are you ready... for some Tic Tac Toe!!!")

while True:

    temp_board = [" "] * 10

    p1_marker, p2_marker = player_input()
    turn = first_player()
    print(turn + " will start the game.")

    play_game = input("Are you sure you want some of this? Enter 'Y' for 'Yes' or 'N' for 'No'")

    if play_game.upper()[0] == 'Y':
        game_on = True
    else:
        game_on = False

    while game_on:
        if turn == "Player 1":
            game_board(temp_board)
            position = player_choice(temp_board)
            place_marker(temp_board, p1_marker, position)

            if check_win(temp_board, p1_marker):
                game_board(temp_board)
                print("Player 1 wins!")
                break
            else:
                if board_check(temp_board):
                    game_board(temp_board)
                    print("Whoa, it's a draw!")
                    game_on = False
                else:
                    turn = "Player 2"
        else:
            game_board(temp_board)
            position = player_choice(temp_board)
            place_marker(temp_board, p2_marker, position)

            if check_win(temp_board, p2_marker):
                game_board(temp_board)
                print("Player 2 wins!")
                game_on = False
            else:
                if board_check(temp_board):
                    game_board(temp_board)
                    print("Whoa, it's a draw!")
                    break
                else:
                    turn = "Player 1"
    
    if not replay():
        break