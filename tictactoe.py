def reset_board():
    # This function Resets the board to its initial values.
    print('Welcome to Tic Tac Toe!')
    # "board" is a list of 10 strings representing the board (ignore index 0)
    board = [' '] * 10


def input_player_letter():
    # Lets the player type which letter they want to be.
    # Returns a list with the player’s letter as the first item, and the computer's letter as the second.
    letter = ''
    while not (letter == 'X' or letter == 'O'):
        print('Do you want to be X or O?')
        letter = input().upper()

    # the first element in the list is the player’s letter, the second is the computer's letter.
    if letter == 'X':
        return ['X', 'O']
    else:
        return ['O', 'X']


reset_board()
input_player_letter()

