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
        # get the indices of the white and black kings
        index_W = board_position.index('W')
        index_B = board_position.index('B')

        # get the proximity of the white and black king pieces to their respective goals and weight the white goal equal to black
        goal_W = index_W + 15
        goal_B = index_B

        # calculate whether or not the white and black kings have support from nearby pieces to prevent a potential reset
        white_support = 0
        black_support = 0

        # determine if the white king has at least one piece nearby to prevent being reset
        # if the white king does have support, reward white for having support from nearby pieces to prevent being reset
        if index_W > 0 and (board_position[index_W + 1] in ['w','b','B']):
            white_support = 5

        # if the black king does have support, reward black for having support from nearby pieces to prevent being reset        
        if index_B < 0 and (board_position[index_B - 1] in ['W','w','b']):
            black_support = 5

        # calculate the penalties for if a white king or a black king could be reset for the next move
        white_reset = 0
        black_reset = 0

        # determine if a king piece could potentially be reset
        # if a white reset is possible, assign a penalty value to white_reset
        if index_W > 0 and (board_position[index_W + 1] in ['b','B']) and board_position[index_W - 1] == 'x':
            white_reset = -20
        
        # if a black reset is possible, assign a penalty value to black_reset
        if index_B < 15 and (board_position[index_B - 1] in ['w','W']) and board_position[index_B + 1] == 'x':
            white_reset = 20

        '''
        the evaluation is the twice the white king's progress to the goal plus its support from the white pawns plus 
        potential white pawn moves plus its reset threat from black minus twice the black king's progress to the goal 
        plus its support from the black pawns plus potential black pawn moves plus its reset threat from white  
        '''
        evaluation = (2 * goal_W + white_support + white_reset) - (2 * goal_B + black_support + black_reset)

        # return the static evaluation value of the current board state
        return evaluation