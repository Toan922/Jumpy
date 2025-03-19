def move_generation(board_state):
    
    # init a positions list to place positions of white pieces into

    positions = []

    '''
    looks through copied board until a w or W is found and places the position of the white pieces 
    into positions list for further evaluation
    '''

    for position, piece in enumerate(board_state):
        if piece == 'W' or piece == 'w':
            positions.append(position)
    
    # create a list of available moves
    
    possible_moves = []
    
    # evaluate all possible moves per white piece in board state
    
    for position in positions:
        # work on a copy of the actual board state every iteration
        
        copy_board = board_state.copy()
        
        # if position of a white piece is at the end of the board make it go out
        
        if position == 15:
            copy_board[position] = 'x'
            possible_moves.append(copy_board)
        
        # if a free space to the right of a white piece then move one to the right
        
        elif copy_board[position + 1] == 'x':
            copy_board[position + 1] = copy_board[position]
            copy_board[position] = 'x'
            possible_moves.append(copy_board)
        
        # compute a possible jump over other pieces
        
        else:
            # see all possible free spaces in the board_state
            
            free_spaces = [index for index, space in enumerate(board_state) if space == 'x']
            
            # compare index of free spaces to white position to see the first empty space to the right
            
            for index in free_spaces:
                # first free space to the right of white position is set to the jump location
                
                if position < index:
                    jump = index
                    break
                
                # no possible jump position so set the jump position to out of board
                
                else:
                    jump = 16
            
            # if jump is out of board then current position is x and return the board
            
            if jump == 16:
                copy_board[position] = 'x'
                possible_moves.append(copy_board)
            else:
                # if a jump is over two pieces then jump over and return the board
                
                if jump - position > 2:
                    copy_board[jump] = copy_board[position]
                    copy_board[position] = 'x'
                    possible_moves.append(copy_board)
                
                # check if a one piece jump is over one white or one black piece
                
                else:
                    # if the piece jumped over is white then just do the jump and return board
                    
                    if copy_board[position + 1] == 'w' or copy_board[position + 1] == 'W':
                        copy_board[jump] = copy_board[position]
                        copy_board[position] = 'x'
                        possible_moves.append(copy_board)
                    
                    # else move the black piece to the left most free space
                    
                    else:
                        copy_board[max(free_spaces)] = copy_board[position + 1]
                        copy_board[jump] = copy_board[position]
                        copy_board[position] = 'x'
                        possible_moves.append(copy_board)