import random


def reset_board():
    # This function Resets the board to its initial values.
    print('Welcome to Tic Tac Toe!')
    # "board" is a list of 10 strings representing the board (ignore index 0)
    board = [' '] * 10
    return board


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


def toss():

    # Randomly choose the player or computer who goes first.
    if random.randint(0, 1) == 0:
        return 'computer'
    else:
        return 'player'


def draw_board(board):

    # This function prints out the board that it was passed.
    # "board" is a list of 10 strings representing the board (ignore index 0)
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('-----------')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('-----------')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])


def is_space_free(board, move):
    # Return true if the passed move is free on the passed board.
    return board[move] == ' '


def get_player_move(board):
    # Let the player type in their move.
    move = ' '
    while move not in '1 2 3 4 5 6 7 8 9'.split():
        print('What is your next move? (1-9)')
        move = input()
    return int(move)


def make_move(board, letter, move):
    if board[move] == ' ':
        board[move] = letter
    else:
        print("You Cant place there")
        new_move = get_player_move(board)
        make_move(board, letter, new_move)


def is_winner(board, letter):
    # Given a board and a player’s letter, this function returns True if that player has won.
    # We use bo instead of board and le instead of letter so we don’t have to type as much.
    return ((board[1] == letter and board[2] == letter and board[3] == letter) or  # across the top
            (board[4] == letter and board[5] == letter and board[6] == letter) or  # across the middle
            (board[7] == letter and board[8] == letter and board[9] == letter) or  # across the bottom
            (board[7] == letter and board[4] == letter and board[1] == letter) or  # down the left side
            (board[8] == letter and board[5] == letter and board[2] == letter) or  # down the middle
            (board[9] == letter and board[6] == letter and board[3] == letter) or  # down the right side
            (board[7] == letter and board[5] == letter and board[3] == letter) or  # diagonal
            (board[9] == letter and board[5] == letter and board[1] == letter))  # diagonal


def is_board_full(board):
    # Return True if every space on the board has been taken. Otherwise return False.
    for i in range(1, 10):
        if is_space_free(board, i):
            return False
    return True


def play_again():
    # This function returns True if the player wants to play again, otherwise it returns False.
    print('Do you want to play again? (yes or no)')
    return input().lower().startswith('y')


def choose_random_move_from_list(board, moves):

    # Returns a valid move from the passed list on the passed board.
    # Returns None if there is no valid move.
    possible_moves = []
    for i in moves:
        if is_space_free(board, i):
            possible_moves.append(i)

    if len(possible_moves) != 0:
        return random.choice(possible_moves)
    else:
        return None


def get_board_copy(board):
    # Make a duplicate of the board list and return it the duplicate.
    dupe_board = []
    for i in board:
        dupe_board.append(i)
    return dupe_board


def get_computer_move(board, computer_letter):
    # Given a board and the computer's letter, determine where to move and return that move.
    if computer_letter == 'X':
        player_letter = 'O'
    else:
        player_letter = 'X'

    # Here is our algorithm for our Tic Tac Toe AI:
    # First, check if we can win in the next move
        for i in range(1, 10):
            copy_board = get_board_copy(board)
            if is_space_free(copy_board, i):
                make_move(copy_board, computer_letter, i)
                if is_winner(copy_board, computer_letter):
                    return i
    
    # Check if the player could win on their next move, and block them.
        for i in range(1, 10):
            copy_board = get_board_copy(board)
            if is_space_free(copy_board, i):
                make_move(copy_board, player_letter, i)
                if is_winner(copy_board, player_letter):
                    return i

    # Try to take one of the corners, if they are free.
    move = choose_random_move_from_list(board, [1, 3, 7, 9])
    if move is not None:
        return move

    # Try to take the center, if it is free.
    if is_space_free(board, 5):
        return 5

    return choose_random_move_from_list(board, [2, 4, 6, 8])


while True:
    reset_board()
    the_board = [' ']*10
    player_letter, computer_letter = input_player_letter()
    turn = toss()
    print('The ' + turn + ' will play first.')
    gameIsPlaying = True

    while gameIsPlaying:
        if turn == 'player':
            # Player’s turn.
            draw_board(the_board)
            move = get_player_move(the_board)
            make_move(the_board, player_letter, move)

            if is_winner(the_board, player_letter):
                draw_board(the_board)
                print('Hooray! You have won the game!')
                gameIsPlaying = False
            else:
                if is_board_full(the_board):
                    draw_board(the_board)
                    print('The game is a tie!')
                    break
                else:
                    turn = 'computer'
        else:
            # Computer’s turn.
            draw_board(the_board)
            move = get_computer_move(the_board, computer_letter)
            print("Computer's Move is", move)
            make_move(the_board, computer_letter, move)

            if is_winner(the_board, computer_letter):
                draw_board(the_board)
                print('The computer has beaten you! You lose.')
                gameIsPlaying = False
            else:
                if is_board_full(the_board):
                    draw_board(the_board)
                    print('The game is a tie!')
                    break
                else:
                    turn = 'player'

    if not play_again():
        break
