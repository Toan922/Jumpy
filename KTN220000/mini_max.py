from static_evaluation import estimate_position as estimate
from generate_move import generate_moves_white as move_white
from generate_move import generate_moves_black as move_black

'''
module designed to recursively generate and evaluate the potential values of the game board states based on the depth
inputted by the user as well as keeping track of how many static evaluations occur in the process
params: depth = the depth of the game tree
        board_state = the current board state
        static_evaluation_counter = counter to keep track of how many static evaluations have occurred

return: the static evaluation of the leaf board states
'''
def max_min(depth: int, board_state: list, static_evaluation_counter: list, game_path: list) -> int:
    # determine the depth of the current game state being evaluated
    
    # when the depth is 0 then a leaf node has been reached and thus static evaluation must be performed
    if depth == 0:
        static_evaluation_counter[0] += 1
        return estimate(board_state)
    # otherwise must recursively call the min_max function to evaluate the next level of the game tree until a leaf node is reached
    else:
        # set the static evaluation to be the lowest possible value
        static_evaluation = -1000
        best_path = None

        #loop through all the potential moves to evaluate their potential children and mini max values if they are a max node
        for possible_position in move_white(board_state):
            # work on a copied version of the game path to keep track of current game path
            current_path = game_path.copy()

            # append the current position to the game path
            current_path.append(possible_position)
            evaluation = max(static_evaluation, min_max(depth - 1, possible_position, static_evaluation_counter, current_path))

            # if the current evaluation is greater than the previous static evaluation then set the game path to be the current path
            if evaluation > static_evaluation:
                static_evaluation = evaluation
                best_path = current_path
        
        if best_path is not None:
            # set the game path to be the best path
            game_path.clear()
            game_path.extend(best_path)

        return evaluation

'''
module designed to recursively generate and evaluate the potential values of the game board states based on the depth
inputted by the user as well as keeping track of how many static evaluations occur in the process
params: depth = the depth of the game tree
        board_state = the current board state
        static_evaluation_counter = counter to keep track of how many static evaluations have occurred

return: the static evaluation of the leaf board states
'''       
def min_max(depth: int, board_state: list, static_evaluation_counter: list, game_path: list) -> int:
    # determine the depth of the current game state being evaluated
    
    # when the depth is 0 then a leaf node has been reached and thus static evaluation must be performed
    if depth == 0:
        static_evaluation_counter[0] += 1
        return estimate(board_state)
    # otherwise must recursively call the min_max function to evaluate the next level of the game tree until a leaf node is reached
    else:
        # set the static evaluation to be the highest possible value
        static_evaluation = 1000
        best_path = None

        for possible_position in move_white(board_state):
            # work on a copied version of the game path to keep track of current game path
            current_path = game_path.copy()

            # append the current position to the game path
            current_path.append(possible_position)
            evaluation = min(static_evaluation, max_min(depth - 1, possible_position, static_evaluation_counter, current_path))

            # if the current evaluation is greater than the previous static evaluation then set the game path to be the current path
            if evaluation < static_evaluation:
                static_evaluation = evaluation
                best_path = current_path
        
        if best_path is not None:
            # set the game path to be the best path
            game_path.clear()
            game_path.extend(best_path)

        return static_evaluation