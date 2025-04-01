'''
module is designed to check whether the white player has won the game by checking if the white king is in the game
params: board_position = the current game board which will be checked for a W piece

returns: True if white has won, False if not won yet
'''

def white_win(board_position: list) -> bool:
    # determine if the white king piece is still in the current board
    if 'W' not in board_position:
        # if the white king is gone then return True
        return True
    else:
        # if the white king is still in the board return False
        return False

'''
module is designed to check whether the black player has won the game by checking if the white king is in the game
params: board_position = the current game board which will be checked for a B piece

returns: True if black has won, False if not won yet
'''

def black_win(board_position: list) -> bool:
    # determine if the black king piece is still in the current board
    if 'B' not in board_position:
        # if the black king is gone then return True
        return True
    else:
        # if the black king is still in the board return False
        return False

'''
module is designed to evaluate the potential value of the current game state in relation to white's winning odds
params: board_position = the current game board which will be checked for a B piece

returns: 100 if white won, -100 if black won, otherwise return (position of W - position of B + 15)
'''

def estimate_position(board_position: list) -> int:
    # determine if white or black has won yet otherwise the potential value of the current game state
    # if white has won then return 100 signifying a static evaluation of 100 for a white win position
    if white_win(board_position):
        return 100
    # if black has won then return -100 signifying a static evaluation of -100 for a black win position
    elif black_win(board_position):
        return -100
    # otherwise return the value from the formula of (position of W - position of B + 15)
    else:
        # get the index of the white king piece
        index_W = board_position.index('W')

        # get the index of the black king piece
        index_B = board_position.index('B')

        # the evaluation is the index of white king minus the index of black king plus 15
        evaluation = index_W - index_B + 15

        # return the static evaluation value of the current board state
        return evaluation