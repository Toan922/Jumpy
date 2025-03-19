def move_generation(board_state):
    
    # init a positions list to place positions of white pieces into

    positions = []

    '''
    looks through copied board until a w or W is found and places the position 
    of the white pieces into positions list for further evaluation
    '''

    for position, piece in enumerate(board_state):
        if piece == 'W' or piece == 'w':
            positions.append(position)
    
    