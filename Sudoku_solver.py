# Bismillah - AbubakarQ #
import os

#-- Other Files --#
import Utility
from AC3 import AC3
from forward_checking import Backtracking_Search

#===============================================================#
""" 
CSCE 4613 - Artifical Intelligence Homework 1
This is problem 4 - Programming Sudoku Solver with CSP. 

Code written by Abubakar Qasim - 010778021.
Test Cases provided by Dr. Thi Hoang Ngan Le.
Backtracking Algorithm walkthrough provided by TechWithTim
AC3 Algorithm referenced from medium.com (Cesar William Alvarenga)
GitHub reference repository: 
https://github.com/aimacode/aima-python/blob/61d695b37c6895902081da1f37baf645b0d2658a/csp.py#L191
"""
#======================================================================= Test Case 1 =======================================================================#
print("\n--------_Test Case 1_---------")

board1 = [
    [5, 3, 4, 6, 7, 8, 9, 0, 0],
    [6, 7, 2, 1, 9, 5, 3, 4, 8],
    [1, 9, 8, 3, 4, 3, 5, 6, 7],
    [8, 5, 9, 7, 6, 1, 4, 2, 3],
    [4, 2, 6, 8, 5, 3, 7, 9, 1],
    [7, 1, 3, 9, 2, 4, 8, 5, 6],
    [9, 6, 1, 5, 3, 7, 2, 8, 4],
    [2, 8, 7, 4, 1, 9, 6, 3, 5],
    [3, 4, 5, 2, 8, 6, 1 ,7 ,9]
]

# Prints Board for current Test Case
print("inital_S - Test_Case_1:\n")
Utility.printBoard(board1)

Utility.menuOption(board1)

#======================================================================= Test Case 2 =======================================================================#
print("\n--------_Test Case 2_---------")

board2 = [
    [0, 8, 0, 0, 0, 0, 0, 0, 1],
    [0, 0, 4, 3, 0, 0, 9, 8, 0],
    [3, 0, 1, 0, 0, 8, 7, 0, 0],
    [0, 1, 0, 5, 4, 0, 0, 6, 0],
    [0, 0, 0, 2, 9, 0, 4, 1, 0],
    [0, 4, 3, 0, 0, 6, 0, 9, 0],
    [0, 0, 8, 0, 0, 5, 0, 3, 0],
    [0, 6, 7, 0, 3, 9, 5, 0, 8],
    [1, 0, 5, 0, 8, 0, 0, 0, 0]
]

# Prints Board for current Test Case
print("inital_S - Test_Case_2:\n")
Utility.printBoard(board2)

Utility.menuOption(board2)

#======================================================================= Test Case 3 =======================================================================#
print("\n--------_Test Case 3_---------")

board3 = [
    [0, 5, 0, 0, 7, 0, 0, 0, 1],
    [8, 7, 6, 0, 2, 1, 9, 0, 3],
    [0, 0, 0, 0, 3, 5, 0, 0, 0],
    [0, 0, 0, 0, 4, 3, 6, 1, 0],
    [0, 4, 0, 0, 0, 9, 0, 0, 2],
    [0, 1, 2, 0, 5, 0, 0, 0, 4],
    [0, 8, 9, 0, 6, 4, 0, 0, 0],
    [0, 0, 0, 0, 0, 7, 0, 0, 0],
    [1, 6, 7, 0, 0, 2, 5, 4, 0]
]

# Prints Board for current Test Case
print("inital_S - Test_Case_3:\n")
Utility.printBoard(board3)

Utility.menuOption(board3)

#================================================================================================#
print("++++++++++++++++ ALL TEST CASES COMPLETE ++++++++++++++++")
print("\n+++ All done, Thank you for using Abubakar's Sudoku Solver! See you soon! +++")
