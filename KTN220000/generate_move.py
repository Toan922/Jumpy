'''
module is designed to generate the potential game states from the original game state after a white piece is moved
and stores the potential game states in a list
params: board_state = the game state to generate moves from

returns: a list which contains all the potential moves that white can make from the original game state
'''
def generate_moves_white(board_state: list) -> list:
    # initialize a positions list to place positions of white pieces into

    positions = []

    '''
    looks through copied board until a w or W is found and places the position of the white pieces 
    into positions list
    '''

    for position, piece in enumerate(board_state):
        if piece == 'W' or piece == 'w':
            positions.append(position)
    
    # create a list of potential moves
    possible_moves = []
    
    # evaluate all possible moves per white piece in board state
    for position in positions:
        # work on a copy of the actual board state every iteration
        copy_board = board_state.copy()

        # determine which kind of move is the piece able to perform
        if position == 15:
            # if the piece is at the end of the board make it leave the game area
            leave_board(position, copy_board, possible_moves)
        elif position + 1 < len(copy_board) and copy_board[position + 1] == 'x':
            # if the piece is able to move one to the right then perform that move
            move_one(position, copy_board, possible_moves)
        else:
            # otherwise the piece is performing a jump
            jumps(position, copy_board, possible_moves)

    return possible_moves

'''
module is designed to generate the potential game states from the original game state after a black piece is moved
and stores the potential game states in a list
params: board_state = the game state to generate moves from

returns: a list which contains all the potential moves that white can make from the original game state
'''
def generate_moves_black(board_state: list) -> list:
    # initialize a positions list to place positions of white pieces into
    positions = []

    # work on a copied and flipped version of the original game board
    copied_flipped_board = board_state.copy()
    flip_board(copied_flipped_board)
    
    '''
    looks through copied board until a w or W is found and places the position of the white pieces 
    into positions list
    '''
    for position, piece in enumerate(board_state):
        if piece == 'W' or piece == 'w':
            positions.append(position)
    
    # create a list of potential moves
    possible_moves = []
    
    # evaluate all possible moves per white piece in board state
    for position in positions:
        # work on a copy of the flipped board state for every iteration
        copy_board = copied_flipped_board.copy()

        # determine which kind of move is the piece able to perform
        if position == 15:
            # if the piece is at the end of the board make it leave the game area
            leave_board(position, copy_board, possible_moves)
        elif position + 1 < len(copy_board) and copy_board[position + 1] == 'x':
            # if the piece is able to move one to the right then perform that move
            move_one(position, copy_board, possible_moves)
        else:
            # otherwise the piece is performing a jump
            jumps(position, copy_board, possible_moves)

    for move in range(len(possible_moves)):
        # flip the board state back to the original orientation and change each piece to be the corresponding opponent piece
        flip_board(possible_moves[move])
    
    return possible_moves

'''
module is designed to flip the game board state such that if a black piece were to be evaluated it would
be evaluated as a white piece
params: position = integer representing where on a 0-15 index that piece is currently 
                -> expected to be 15 in this case
        game_board = the copied version of the original game board
        potential_moves = a list housing all the potential board states based on which piece moved
'''
def flip_board(game_board: list):
    # reverse the board state to evaluate black pieces as if they were white pieces
    game_board.reverse()
    
    # changes each piece into the corresponding opponent piece i.e B <-> W and b <-> w
    for index in range(len(game_board)):
        # set the current piece to be whatever value is in the current index
        piece = game_board[index]
        
        # determine if the piece is white or black and more specifically if it is a king or pawn piece
        if piece == 'B':
            # if the piece is a black king set it to be the white king
            game_board[index] = 'W'
        elif piece == 'b':
            # if the piece is a black pawn set it to be the white pawn
            game_board[index] = 'w'
        elif piece == 'W':
            # if the piece is a white king set it to be the black king
            game_board[index] = 'B'
        elif piece == 'w':
            # if the piece is a white pawn set it to be the black pawn
            game_board[index] = 'b'

'''
module is designed to generate the game board state after a piece has left the game area and
append that board state to the potential moves list
params: position = integer representing where on a 0-15 index that piece is currently 
                -> expected to be 15 in this case
        game_board = the copied version of the original game board
        potential_moves = a list housing all the potential board states based on which piece moved
'''
def leave_board(position: int, game_board: list, potential_moves: list):
    # sets the last space to be a free space and appends this new board to potential moves
    game_board[position] = 'x'
    potential_moves.append(game_board)

'''
module is designed to generate the game board state after a piece has moved one space and
append that board state to the potential moves list
params: position = integer representing where on a 0-15 index that piece is currently
        game_board = the copied version of the original game board
        potential_moves = a list housing all the potential board states based on which piece moved
'''
def move_one(position: int, game_board: list, potential_moves: list):
    # set the next space to the right as the piece moving and the previous space as a free space
    game_board[position + 1] = game_board[position]
    game_board[position] = 'x'

    # append the new board state to the potential moves list
    potential_moves.append(game_board)

'''
module is designed to generate the game board state after a piece has left the game area and
append that board state to the potential moves list
params: position = integer representing where on a 0-15 index that piece is currently
        game_board = the copied version of the original game board
        potential_moves = a list housing all the potential board states based on which piece moved
'''
def jumps(position: int, game_board: list, potential_moves: list):
    jump = None
    
    # see all possible free spaces in the board_state
    free_spaces = [index for index, space in enumerate(game_board) if space == 'x']
    
    # compare index of free spaces to white position to see the first empty space to the right
    for index in free_spaces:
        # determine if the white piece has any free spaces to the right of it
        if position < index:
            # there is a free space to to the right so set the position of that free space as the jump location
            jump = index
            break

    # determine how many spaces the jump is meant to go over
    
    # if the jump is set to be out of the board then set the current position to a free space
    if jump == None:
        game_board[position] = 'x'
        potential_moves.append(game_board)
        
    # otherwise if the jump is over 2 pieces then set the jump location as the current piece and the original position as free
    elif jump - position > 2:
        game_board[jump] = game_board[position]
        game_board[position] = 'x'
        potential_moves.append(game_board)
        
    # otherwise if the piece jumped over is white thus perform the jump and append the board state to potential moves
    elif game_board[position + 1] == 'w' or game_board[position + 1] == 'W':
        game_board[jump] = game_board[position]
        game_board[position] = 'x'
        potential_moves.append(game_board)
        
    # otherwise if the piece jumped over is a black piece thus reset the black piece to the rightmost free space
    elif game_board[position + 1] == 'b' or game_board[position + 1] == 'B':
        # perform the white jump and free up the current white space and append the new board state to potential moves list
        game_board[jump] = game_board[position]
        game_board[position] = 'x'
        
        # recheck all possible free spaces in the board_state
        free_spaces = [index for index, space in enumerate(game_board) if space == 'x']

        # determine if the black piece that was jumped over is past the rightmost free space
        # if the rightmost free space is greater than the jump then set the black piece to be the rightmost free space
        if max(free_spaces) > position + 1:
            game_board[max(free_spaces)] = game_board[position + 1]
            game_board[position + 1] = 'x'
        
        potential_moves.append(game_board)