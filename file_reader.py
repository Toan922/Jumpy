def reader(board1_name: str) -> list:
    # tries to read the file used as argument 1 within the command line input, if it does not exist then print an error message

    try:
        # opens the board1 file and extracts the board state from the file as a string

        with open(board1_name, "r") as reader:
            board_string = reader.read()
    
        # takes the board state in string form and extracts each character to place into an array to be returned
    
        board_state = list(board_string)

        reader.close()

        return board_state
    
    # if a file does not exist then print the file not found message w/ the file name
    
    except FileNotFoundError:
        print(f"The {board1_name} file does not exist, please try again with the correct file name")


def writer(board2_name: str, board_str: str):
    # writes to the board2 file with the determined "optimal" game state after white's move

    with open(board2_name, "w") as writer:
        writer.write(board_str)

    writer.close()
