# Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

# Each row must contain the digits 1-9 without repetition.
# Each column must contain the digits 1-9 without repetition.
# Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
# Note:

# A Sudoku board (partially filled) could be valid but is not necessarily solvable.
# Only the filled cells need to be validated according to the mentioned rules.
 

# Example 1:


# Input: board = 
# [["5","3",".",".","7",".",".",".","."]
# ,["6",".",".","1","9","5",".",".","."]
# ,[".","9","8",".",".",".",".","6","."]
# ,["8",".",".",".","6",".",".",".","3"]
# ,["4",".",".","8",".","3",".",".","1"]
# ,["7",".",".",".","2",".",".",".","6"]
# ,[".","6",".",".",".",".","2","8","."]
# ,[".",".",".","4","1","9",".",".","5"]
# ,[".",".",".",".","8",".",".","7","9"]]
# Output: true
# Example 2:

# Input: board = 
# [["8","3",".",".","7",".",".",".","."]
# ,["6",".",".","1","9","5",".",".","."]
# ,[".","9","8",".",".",".",".","6","."]
# ,["8",".",".",".","6",".",".",".","3"]
# ,["4",".",".","8",".","3",".",".","1"]
# ,["7",".",".",".","2",".",".",".","6"]
# ,[".","6",".",".",".",".","2","8","."]
# ,[".",".",".","4","1","9",".",".","5"]
# ,[".",".",".",".","8",".",".","7","9"]]
# Output: false
# Explanation: Same as Example 1, except with the 5 in the top left corner being modified to 8. Since there are two 8's in the top left 3x3 sub-box, it is invalid.
 

# Constraints:

# board.length == 9
# board[i].length == 9
# board[i][j] is a digit 1-9 or '.'.

def isValidSudoku(board):

# Implementing the same with small changes to see if it improves performance
# (checking c and using continue instead of checking it using if condition each time saved around 20ms)
    rows = []
    cols = [{} for _ in range(0,9)]
    box = [{} for _ in range(0,9)]

    for row in range(0,9):
        rowDict = {}
        for col in range(0,9):
            c = board[row][col]
            if c == ".":
                continue
            if c in rowDict:
                return False
            else:
                rowDict[c] = 1
            
            if c in cols[col]:
                return False
            else:
                cols[col][c] = 1
            
            boxNum = 3*(row//3) + (col//3)

            if c in box[boxNum]:
                return False
            else:
                box[boxNum][c] = 1
            
        rows.append(rowDict)
    return True

    # Solution implemented by discussing with Sudharshan
    # He suggested to use the 2D approach which saved lot of time and provided approach
    # rows = []
    # cols = [{} for _ in range(0,9)]
    # box = [{} for _ in range(0,9)]

    # for row in range(0,9):
    #     rowDict = {}
    #     for col in range(0,9):
    #         if board[row][col] in rowDict:
    #             return False
    #         elif board[row][col] != ".":
    #             rowDict[board[row][col]] = 1
            
    #         if board[row][col] in cols[col]:
    #             return False
    #         elif board[row][col] != ".":
    #             cols[col][board[row][col]] = 1
            
    #         if board[row][col] in box[3*(row//3) + (col//3)]:
    #             return False
    #         elif board[row][col] != ".":
    #             box[3*(row//3) + (col//3)][board[row][col]] = 1
            
    #     rows.append(rowDict)
    # return True


if __name__ == "__main__":
    board = [["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
    
    print(isValidSudoku(board))