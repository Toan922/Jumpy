                             ,---._                          ____  ,-.----.                 
                           .-- -.' \                       ,'  , `.\    /  \                
                           |    |   :         ,--,      ,-+-,.' _ ||   :    \         ,---, 
                           :    ;   |       ,'_ /|   ,-+-. ;   , |||   |  .\ :       /_ ./| 
                           :        |  .--. |  | :  ,--.'|'   |  ;|.   :  |: | ,---, |  ' : 
                           |    :   :,'_ /| :  . | |   |  ,', |  ':|   |   \ :/___/ \.  : | 
                           :         |  ' | |  . . |   | /  | |  |||   : .   / .  \  \ ,' ' 
                           |    ;   ||  | ' |  | | '   | :  | :  |,;   | |`-'   \  ;  `  ,' 
                       ___ l         :  | | :  ' ; ;   . |  ; |--' |   | ;       \  \    '  
                     /    /\    J   :|  ; ' |  | ' |   : |  | ,    :   ' |        '  \   |  
                    /  ../  `..-    ,:  | : ;  ; | |   : '  |/     :   : :         \  ;  ;  
                    \    \         ; '  :  `--'   \;   | |`-'      |   | :          :  \  \ 
                     \    \      ,'  :  ,      .-./|   ;/          `---'.|           \  ' ; 
                      "---....--'     `--`----'    '---'             `---`            `--`                
This is a class project for CS 4365 led by Professor Schweitzer where the program
plays the game Jumpy

Jumpy is a game in which the user plays as either white or black, with a goal of removing their
king piece (represented as a W or B) from the game board before the opponent does

The rules for Jumpy are as follows:
    A white piece moves to the right and can only move 1 space to the right unless a jump occurs
    A black piece moves to the left and can only move 1 space to the left unless a jump occurs

    A jump occurs when the immediate space in the direction of a piece's move is occupied by another piece
    When this occurs the piece jumps over the occupied spaces until it finds the next free space

    Jumping has a special rule which only applies if a piece jumps over exactly 1 piece which is also an opponent piece:
        If the condition of a single piece is jumped over and that piece is an opponent then it is "reset" back to the
        leftmost free space if it is white and rightmost free space if it is black

This program is split into 4 sections, MiniMax.py, AlphaBeta.py, MiniMaxBlack.py, and MiniMaxImproved.py
    
To run the program, do the following in command line: python -m {section chosen} {file 1} {file 2} {depth}
    section chosen = one of the four sections chosen to be tested
    file 1 = the file containing the initial board state to be evaluated
    file 2 = the file that the evaluated move should be written to
    depth = depth the game tree should be evaluated to

MiniMax.py is designed to evaluate the best move for the white player from the board state in file 1 with a Mini-Max algorithm using the provided static evaluation formula from class

AlphaBeta.py is designed to evaluate the best move for the white player from the board state in file 1 with an Alpha-Beta pruning algorithm using the provided static evaluation formula from class

MiniMaxBlack.py is designed to evaluate the best move for the black player from the board state in file 1 with a Mini-Max algorithm using the provided static evaluation formula from class

MiniMaxImproved.py is designed to evaluate the best move for the white player from the board state in file 1 with a Mini-Max algorithm using the a self-made static evaluation formula which is designed to improve on the static evaluation formula from class

Ways that my static evaluation is considered "better" than the provided static evaluation:
    It considers if a king piece is potentially reset for the next move and penalizes the respective player for it
        This improves on the old static evaluation which did not consider this possibility as it makes it so that the game does not play a position where the white king is able to be reset by the black player for the next move
    It considers if a king piece has support from surrounding pieces which would prevent a potential reset further along
        This improves on the old static evaluation as it rewards the white player for a position in which the white king is not put in a position where it could be reset a few moves past the desired evaluated depth
    It emphasizes the weighting of the king piece's progress towards their respective goals
        This improves on the old static evaluation as it places a heavier emphasis on moving the white king towards the goal of removing it from the game board
