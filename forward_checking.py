# Bismillah - AbubakarQ #
import os

#-- Other Files --#
import Utility

#===============================================================#

def Backtracking_Search(board):
    """
    Recusive Function - Backtracking begins here
    """

    # Boolean Value for board
    find = Utility.find_empty(board)

    # Recursion to identify if empty slot found
    if not find:
        return True
    else: 
        row, col = find

    # Loops through values 1 - 10 (1 - 9)
    for i in range(1,10):
        # if validity returns True, value is added 
        if Utility.validity(board, i, (row, col)):
            # row, col is set to current integer from range if valididity test is passed
            board[row][col] = i

            # Recursive solution to keep calling Algorithm to test all values from range 1-9 to check if solution is correct
            if Backtracking_Search(board):
                return True

            # If all values are tried and Sudoku is still not solved, return 0 to BACKTRACK to recursively solve previous empty states
            board[row][col] = 0

    # When all values fail, backtracked initiated here returning false returning to previous solution. 
    return False

