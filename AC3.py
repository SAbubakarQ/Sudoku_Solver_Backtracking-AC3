# Bismillah - AbubakarQ #
import os

#-- Other Files --#
import Utility

#===============================================================#

def AC3(board):
    
    # board to a queue
    queue = board[:]

    # repeats until queue is empty
    while queue:
        # Take the first 'arc' off the queue
        (x, y) = queue.pop(0)

        # Making x arc consistent with y
        revised = Utility.revise(board, x, y)

        # If the x domain changed:
        if revised:
            neighbors = [neighbor for neighbor in board if neighbor[1] == x]
            queue = queue + neighbors
