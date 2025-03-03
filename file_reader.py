def reader(board1_name):

    # opens the board1 file and extracts the board state from the file as a string

    with open(board1_name, "r") as reader:
        board_string = reader.read()
    
    # takes the board state in string form and extracts each character to place into an array to be returned
    
    board_state = list(board_string)

    reader.close()

    return board_state

def writer(board2_name, board_list):

    # joins the board list back together as a string to be written to board2 file
    board_string = "".join(board_list)

    # writes to the board2 file with the determined "optimal" game state after white's move

    with open(board2_name, "w") as writer:
        writer.write(board_string)

    writer.close()
