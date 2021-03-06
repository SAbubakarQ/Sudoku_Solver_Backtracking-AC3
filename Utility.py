# Bismillah - AbubakarQ #
import os

#-- Other Files --#
import AC3
import forward_checking

#=============================================================================================#

# Printing Board (Tutorial Demonstration from TechWithTime)
def printBoard(board):
    for i in range(len(board)):
        # Print dividng line amongst columns (Each array)
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - - - -")
        #prints divider between every three integers (Inside of array) 
        for j in range(len(board[0])):
            if j % 3 == 0 and j != 0:
                print("| ", end="")
            
            if j == 8:
                print(board[i][j])
            else:
                print(str(board[i][j]) + "  ", end="")
    print("\n")

# Asking User for input
def menuOption(board):
    print("Which algorithm would you like to use?\n A - Backtracking + Forward Checking\n B - Arc Consistency\n X - Next Test Case\n")
    choice = input("Choice: ")

    while choice != 'X':

        if (choice == 'A' or choice == 'a'):
            print("\n--Backtracking + Forward Checking--\n")
            # Begin Backtracking/Forward Checking algorthim
            try:
                forward_checking.Backtracking_Search(board)
            except:
                print("Error...Try Again\n")
            print("Solution for Test Case:\n")
            print("solution_S:\n")
            printBoard(board)
            print("How would you like to continue?\n A - Backtracking + Forward Checking\n B - Arc Consistency\n X - Next Test Case\n")
            choice = input("Choice: ")

        elif (choice == 'B' or choice == 'b'):
            print("\n--Arc Consistency--\n")
            # Begin Arc Consistency Algorithm
            try:
                AC3.AC3(board)
            except:
                print("Error...Issue with AC3 Algorithm\n")
            print("How would you like to continue?\n A - Backtracking + Forward Checking\n B - Arc Consistency\n X - Next Test Case\n")
            choice = input("Choice: ")

        else:
            print("\nMoving to Next Test ->")
            break

#============================_Backtracking/Forward Checking_===================================#

def find_empty(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0:
                return (i, j) # row, column

    return None

def validity(board, number, pos):
    # Sudoku Rules:

    # Checking Row
    # looping through each column
    for i in range(len(board[0])):
        # checking each element in the row and see if equal to number just added in
        if board[pos[0]][i] == number and pos[1] != i:
            return False

    # Checking Column
    # looping through each row 
    for i in range(len(board)):
        # similar yet checking each column instead of row for match
        if board[i][pos[1]] == number and pos[0] != i:
            return False

    # Checking 9x9 Box
    box_x = pos[1] // 3
    box_y = pos[0] // 3

    """
    This code below gets the index for the appropriate box within the 9x9 board
    """
    # looping through each 9 element for each box
    for i in range(box_y * 3, box_y * 3 + 3):
        for j in range(box_x * 3, box_x * 3 + 3):
            if board[i][j] == number and (i, j) != pos:
                return False

    return True



#==================================_Arc Consistency 3_=========================================#

# # Revise Function pertaining to Arc Consistency
def revise(board, x, y):
    """
    Creating variable x arc consistent with y.
    If value removed, returns True
    """

    revised = False 

    # Obtaining Domains from Board
    x_domain = board[x]
    y_domain = board[y]

    # Geting all arc constraints with use of validity from
    # Backracking algorithm
    allConstraints = [
        constraint for constraint in board if constraint[0] == x and constraint[1] == y
    ]
    
    for x_value in x_domain:
        satisfies = False
        for y_value in y_domain:
            for constraint in allConstraints:
                constraint_func = board[constraint]
                if constraint_func(x_value, y_value):
                    satisfies = True
        if not satisfies:
            x.domain.remove(x_value)
            revised = True

    return revised
