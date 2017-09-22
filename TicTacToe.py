# Tic-Tac-Toe.

import random


def draw_board(board):
    # This function prints out the board it was passed.

    #'Board' is a list of 10 strings representing the board(ignore index 0)
    print(board[7] + '|' + board[8] + '|' + board[9])
    print('-+-+-')
    print(board[4] + '|' + board[5] + '|' + board[6])
    print('-+-+-')
    print(board[1] + '|' + board[2] + '|' + board[3])


def input_player_letter():
    # Lets the player type what letter they want to be.
    # Returns a list with the player's letter as the first item and the computer's as the second.
    letter = ' '
    while not(letter == 'X' or letter == 'O'):
        print('Do you want to be X or O?')
        letter = input() .upper()

        # First element in list is the players letter, second is the computers.
    if letter == 'X':
        return['X', 'O']
    else:
        return['O', 'X']


def who_goes_first():
    # Randomly chooses who goes first.
    if random.randint(0, 1) == 0:
        return 'Computer'
    else:
        return 'Player'


def make_move(board, letter, move): 
    board[move] = letter
        

def is_winner(bo, le):
    # Given a board and a players letter, this function returns True if the player won.

    return((bo[7] == le and bo[8] == le and bo[9] == le) or  # Across the top.
           # Across the middle.
           (bo[4] == le and bo[5] == le and bo[6] == le) or
           # Across the bottom.
           (bo[1] == le and bo[2] == le and bo[3] == le) or
           # Down the left side.
           (bo[7] == le and bo[4] == le and bo[1] == le) or
            # Down the middle.
           (bo[8] == le and bo[5] == le and bo[2] == le) or
           # Down the right side.
           (bo[9] == le and bo[6] == le and bo[3] == le) or
            # Diagonal.
           (bo[7] == le and bo[5] == le and bo[3] == le) or 
            # Diagonal.
           (bo[9] == le and bo[5] == le and bo[1] == le)) 


def get_board_copy(board):
    # Make a copy of the board and return it.
    board_copy = []
    for i in board:
        board_copy.append(i)
    return board_copy


def is_space_free(board, move):
    # Return True if the passed move is free on the passed board.
    return board[move] == ' '


def get_player_move(board):
    # lets the player enter their move.
    move = ' '
    while move not in '1 2 3 4 5 6 7 8 9'.split() or not is_space_free(board, int(move)):
        print('What is your next move? (1-9) ')
        move = input()
    return int(move)


def choose_random_move_from_list(board, moves_list):
    # Returns a valid move from the passed list on the passed board.
    # Returns None if there is no valid move.
    possible_moves = []
    for i in moves_list:
        if is_space_free(board, i):
            possible_moves.append(i)

    if len(possible_moves) != 0:
        return random.choice(possible_moves)
    else:
        return None


def get_computer_move(board, computer_letter):
    # Given a board and the computers letter, determine where to move and return that move.
    if computer_letter == 'X':
        player_letter = 'O'
    else:
        player_letter = 'X'

     # This is the algorithm for the TTT AI
    # First check if we can win in the next move.
    for i in range(1, 10):
        board_copy = get_board_copy(board)
        if is_space_free(board, i):
            make_move(board_copy, computer_letter, i)
            if is_winner(board_copy, computer_letter):
                return i

    # Check if player could win on their next move and block them.
    for i in range(1, 10):
        board_copy = get_board_copy(board)
        if is_space_free(board_copy, i):
            make_move(board_copy, player_letter, i)
            if is_winner(board_copy, player_letter):
                return i

    # Try to take one of the corners if they are free.
    move = choose_random_move_from_list(board, [1, 3, 7, 9])
    if move != None:
        return move

    # Try to take the center if it is free.
    if is_space_free(board, 5):
        return 5

    # Move on one of the sides.
    return choose_random_move_from_list(board,[2, 4, 6, 8])


def is_board_full(board):
    # Returns True if every space on the board has been taken, otherwise return False.
    for i in range(1, 10):
        if is_space_free(board, i):
            return False
    return True


print('Welcome to Tic Tac Toe!')

while True:
    # Reset the board.
    the_board = [' '] * 10
    player_letter, computer_letter = input_player_letter()
    turn = who_goes_first()
    print('The ' + turn + ' will go first.')
    game_is_playing = True

    while game_is_playing:
        if turn == 'player':
            # Player's turn.
            draw_board(the_board)
            move = get_player_move(the_board)
            make_move(the_board, player_letter, move)

            if is_winner(the_board, player_letter):
                draw_board(the_board)
                print('Hooray! You have won the game!')
                game_is_playing = False
            else:
                if is_board_full(the_board):
                    draw_board(the_board)
                    print('The game is a tie!')
                    break
                else:
                    turn = 'computer'

        else:
            # Computer's turn
            move = get_computer_move(the_board, computer_letter)
            make_move(the_board, computer_letter, move)
        

            if is_winner(the_board, computer_letter):
                draw_board(the_board)
                print('The computer has beaten you! You lose.')
                game_is_playing = False
            else:
                if is_board_full(the_board):
                    draw_board(the_board)
                    print('The game is a tie!')
                    break
                else:
                    turn = 'player'

    print('Do you want to play again? (yes or no )')
    if not input() .lower() .startswith('y'):
        break
