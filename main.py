from file_reader import reader, writer

def main():
    board_state = reader("board1.txt")

    print(board_state)

    writer("board2.txt", board_state)

if __name__ == "__main__":
    main()