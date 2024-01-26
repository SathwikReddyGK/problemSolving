# Description
# Given an m x n grid of characters board and a string word, return true if word exists in the grid.

# The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.

 

# Example 1:


# Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
# Output: true
# Example 2:


# Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE"
# Output: true
# Example 3:


# Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB"
# Output: false
 

# Constraints:

# m == board.length
# n = board[i].length
# 1 <= m, n <= 6
# 1 <= word.length <= 15
# board and word consists of only lowercase and uppercase English letters.
 

# Follow up: Could you use search pruning to make your solution faster with a larger board?

# Solution

# // Time Complexity : O((m*n)4^L), m-number of row, n-number of cols, L - length of word. Since we are iterating over the entire
#                      matrix and wherever we find word character from their we start recursion and that recursion can go upto
#                      the length of the word. In recursion we always look into all the 4 sides of that cell, so for each cell
#                      there are four options. It is ideally three options, since we are already coming from one direction.
#                      But we can consider 4 when generalising. Since we might see failures at almost all cells, worst case is 
#                      O((m*n)4^L)               
# // Space Complexity : O(L), L is the length of the word. Because of implicit stack of recursion.
# 
# // Did this code successfully run on Leetcode : Yes
# // Any problem you faced while coding this : None


# // Your code here along with comments explaining your approach
# Approach is we check each cell in matrix to see if the value is matching with first character of words, if matches then we can
# start recursion to see if one of the 4 adjacent cells(horizontal and vertical) are matching with second category, if matches
# then continue recursion to check if the 4 adjacent cells(horizontal and vertical) of the new cell are matching with third
# character and so on. We need to make sure we are marking a cell as visited(I made it space here) so that we do not end up coming
# back to the same cell.

def exist(board,word):
    def backtracking(matrix,row,col,idx,rowLen,colLen):
        
        if idx>=len(word):
            return True
        
        if row>0 and matrix[row-1][col] == word[idx]:
            temp = matrix[row-1][col]
            matrix[row-1][col] = ""
            result = backtracking(matrix,row-1,col,idx+1,rowLen,colLen)
            if result == True:
                return True
            else:
                matrix[row-1][col] = temp
        if col>0 and matrix[row][col-1] == word[idx]:
            temp = matrix[row][col-1]
            matrix[row][col-1] = ""
            result = backtracking(matrix,row,col-1,idx+1,rowLen,colLen)
            if result == True:
                return True
            else:
                matrix[row][col-1] = temp
        if row+1<rowLen and matrix[row+1][col] == word[idx]:
            temp = matrix[row+1][col]
            matrix[row+1][col] = ""
            result = backtracking(matrix,row+1,col,idx+1,rowLen,colLen)
            if result == True:
                return True
            else:
                matrix[row+1][col] = temp
        if col+1<colLen and matrix[row][col+1] == word[idx]:
            temp = matrix[row][col+1]
            matrix[row][col+1] = ""
            result = backtracking(matrix,row,col+1,idx+1,rowLen,colLen)
            if result == True:
                return True
            else:
                matrix[row][col+1] = temp
        
    m = len(board)
    n = len(board[0])
    for row in range(0,m):
        for col in range(0,n):
            if board[row][col] == word[0]:
                temp = board[row][col]
                board[row][col] = ""
                result = backtracking(board,row,col,1,m,n)
                if result == True:
                    return True
                else:
                    board[row][col] = temp
    
    return False

if __name__ == "__main__":
    board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
    word = "ABCCED"
    print(exist(board,word))