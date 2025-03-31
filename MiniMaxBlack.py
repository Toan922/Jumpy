#!/usr/bin/env python
# this is for running the script in the bash terminal of codespaces

from file_reader import reader as read, writer as write
from generate_move import generate_moves_black as make_moves, flip_board as flip
from mini_max import max_min as mini_max
import sys

'''
This module is designed to take the file names of boards 1 and 2 with 1 = initial position and
2 = determined move file, after taking those as arguments in the command line, the program then evaluates
the best move for black and writes that to the second board file
'''

def black_move():
    # gets the board name for the initial position board file from the first command line argument
    initial_board = sys.argv[1]
    move_board = sys.argv[2]
    
    # gets the depth to be evaluated to for the MiniMax algorithm
    depth_evaluated = int(sys.argv[3])
    
    # reads the board state from the initial board file as a list to then be evaluated
    board_state = read(initial_board)

    # a counter to determine how many times static evaluation occurs
    static_evaluation_counter = [0]
    
    # generates all immediate possible moves given the current position and stores them in a list
    potential_moves = make_moves(board_state)
    
    game_path = []
    
    # get the value of the highest static evaluation from mini max being performed
    static_evaluation = mini_max(depth_evaluated, board_state, static_evaluation_counter, game_path)

    # reverse the game_path to get the correct orientation since it was evaluated as a white move
    for index in range(len(game_path)):
        flip(game_path[index])

    for move in potential_moves:
        # check which move is the progenitor of the best path
        if move == game_path[0]:
            # set the move to be the best path
            optimal_move = move
            break

    # convert the optimal move to a string
    optimal_move = ''.join(optimal_move)

    # write the optimal move to the move board file
    write(move_board, optimal_move)

    # prints out the optimal move
    print(f"Output board position: {optimal_move}")

    # prints out the amount of times static evaluation has occurred
    print(f"Positions evaluated by static evaluation: {static_evaluation_counter[0]}")

    # prints out the estimate of the mini max value of the optimal move
    print(f"MINIMAX estimate: {static_evaluation}")

if __name__ == "__main__":
    black_move()