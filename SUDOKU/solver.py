"""
# Title for board
print("")
print("-------------------")
print("MY SUDOKU ALGORITHM")
print("-------------------")
print("")

# Prints out the board
SudokuBoard = [
              [0, 0, 0, 0, 0, 4, 0, 9, 0],
              [8, 0, 2, 9, 7, 0, 0, 0, 0], 
              [9, 0, 1, 2, 0, 0, 3, 0, 0], 
              [0, 0, 0, 0, 4, 9, 1, 5, 7], 
              [0, 1, 3, 0, 5, 0, 9, 2, 0], 
              [5, 7, 9, 1, 2, 0, 0, 0, 0], 
              [0, 0, 7, 0, 0, 2, 6, 0, 3],
              [0, 0, 0, 0, 3, 8, 2, 0, 5], 
              [0, 2, 0, 5, 0, 0, 0, 0, 0]
]
"""
# Algorithm that will use the available functions and backtrack for us. 
def solve(board): 
    
    # Finding an empty board. 
    find = find_empty(board)

    # Function returns if we had found the solution. 
    if not find: 
        return True

    else: 
        row, column = find

    # We loop from the values 1 to 9, and attempt to put those into our solution.  
    for i in range(1, 10): 

        # Checks by adding into our board that it will be a valid solution.   
        if valid(board, i, (row, column)): 

            # If it is valid, then we will add it into our board. 
            board[row][column] = i

            # Recursively try to finish the solution by calling solve on our new board.
            # Basically go through the same process multiple times until we find the solution or had looped through all the different numbers until none of them are valid.    
            if solve(board):
                return True

            # If it is false, then reset the last element we just added when it is incorrect. 
            board[row][column] = 0

    # If we loop through all the numbers and none of them are valid, we will return False meaning that solve isn't going to be true
    return False           

# Makes sure that the given board is valid. 
def valid(board, number, position): 

    # Check row
    for i in range(len(board[0])):

        # Checks through each column in the row and that it is equal to the number we add in. 
        if board[position[0]][i] == number and position[1] != i:
            return False
    
    # Check column that loops through every row from 0 to 9.
    for i in range(len(board)):

        # Checks to see if the colum value is equal to the same number we have inserted and not in the exact position. 
        if board[i][position[1]] == number and position[0] != i:
            return False

    # Check box (determines which of the 9 boxes we are in)
    box_x = position[1] // 3 # The 3 will give us the values 0, 1, and 2. 
    box_y = position[0] // 3 # The 3 will give us the values 0, 1, and 2.

    # Loop through all nine elements in the box to make sure we don't have the same element appearing twice. 
    for i in range(box_y * 3, box_y*3 + 3):
        for j in range(box_x * 3, box_x*3 + 3):

            # We loop through the box and check if any other element in the box is 
            # equal to the one we just added, and not check the same position we just added in. 
            if board[i][j] == number and (i,j) != position: 
                return False # When we found a duplicate. 

        # If we make it to the end of all these checks, then that means everything is fine. 
        return True


# Function for a visual representation of the board. 
def print_board(board): 
    for i in range(len(board)): 
        
        # After three rows on the board, this will print out the "- - - - - -"
        if i % 3 == 0 and i != 0: 
            print("- - - - - - - - - - - - - -")
        
        # For every position in the row. 
        for j in range(len(board[0])):

            # Checks if it is the third element (a multiple of 3) to draw the horizontal line. 
            if j % 3 == 0 and j != 0: 
                print(" | ", end="")
            
            # Checks to see if we are at the last position. 
            if j == 8: 
                print(board[i][j])
            else: 
                print(str(board[i][j]) + " ", end="") # This means to stay on the same line. 

# Give a board to find an empty square.
def find_empty(board): 
    for i in range(len(board)): 
        for j in range(len(board[0])): 

            # Checks to see if the position is 0.
            if board[i][j] == 0: 
                return (i, j) # row, column

    return None # If there are no blank squares on the board. 
"""
# Shows the unsolved solution. 
print_board(SudokuBoard) 

# Solves the solution.
solve(SudokuBoard) 

# Gives space to have a better visual for the output. 
print("________________________________")

# Prints message for the solved sudoku. 
print("")
print("-------------------")
print("SUDOKU SOLVED")
print("-------------------")
print("")

# Shows the solved solution. 
print_board(SudokuBoard)

"""