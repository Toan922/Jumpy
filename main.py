from file_reader import reader, writer
from move_evaluation import move_generation as moves

def main():
    board_state = reader("board1.txt")

    moves(board_state)

    writer("board2.txt", board_state)

if __name__ == "__main__":
    main()