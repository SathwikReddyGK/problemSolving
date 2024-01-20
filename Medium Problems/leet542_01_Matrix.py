# Description
# Given an m x n binary matrix mat, return the distance of the nearest 0 for each cell.

# The distance between two adjacent cells is 1.

 

# Example 1:


# Input: mat = [[0,0,0],[0,1,0],[0,0,0]]
# Output: [[0,0,0],[0,1,0],[0,0,0]]
# Example 2:


# Input: mat = [[0,0,0],[0,1,0],[1,1,1]]
# Output: [[0,0,0],[0,1,0],[1,2,1]]
 

# Constraints:

# m == mat.length
# n == mat[i].length
# 1 <= m, n <= 104
# 1 <= m * n <= 104
# mat[i][j] is either 0 or 1.
# There is at least one 0 in mat.

# Solution

# // Time Complexity : 
# // Space Complexity :
# // Did this code successfully run on Leetcode :
# // Any problem you faced while coding this : 


# // Your code here along with comments explaining your approach
# Approach is 

from collections import deque

def updateMatrix(mat):
    greedyQueue = deque()
    rowNum = len(mat)
    colNum = len(mat[0])
    for i in range(rowNum):
        for j in range(colNum):
            if mat[i][j] == 0:
                greedyQueue.append((i,j))
            else:
                mat[i][j] *= -1
    
    while greedyQueue:
        rowCol = greedyQueue.popleft()

        if rowCol[0] > 0 and ( mat[rowCol[0]-1][rowCol[1]] < 0): #or (mat[rowCol[0]-1][rowCol[1]] > 0 and mat[rowCol[0]-1][rowCol[1]] < mat[rowCol[0]][rowCol[1]] )):
            mat[rowCol[0]-1][rowCol[1]] = mat[rowCol[0]][rowCol[1]] + 1
            greedyQueue.append((rowCol[0]-1,rowCol[1]))
        elif rowCol[1] > 0 and ( mat[rowCol[0]][rowCol[1]-1] < 0): #or (mat[rowCol[0]][rowCol[1]-1] > 0 and mat[rowCol[0]][rowCol[1]-1] < mat[rowCol[0]][rowCol[1]] )):
            mat[rowCol[0]][rowCol[1]-1] = mat[rowCol[0]][rowCol[1]] + 1
            greedyQueue.append((rowCol[0],rowCol[1]-1))
        elif rowCol[0]+1 < rowNum and ( mat[rowCol[0]+1][rowCol[1]] < 0): #or (mat[rowCol[0]+1][rowCol[1]] > 0 and mat[rowCol[0]+1][rowCol[1]] < mat[rowCol[0]][rowCol[1]] )):
             mat[rowCol[0]+1][rowCol[1]] = mat[rowCol[0]][rowCol[1]] + 1
             greedyQueue.append((rowCol[0]+1,rowCol[1]))
        elif rowCol[1]+1 < colNum and ( mat[rowCol[0]][rowCol[1]+1] < 0): #or (mat[rowCol[0]][rowCol[1]+1] > 0 and mat[rowCol[0]][rowCol[1]+1] < mat[rowCol[0]][rowCol[1]] )):
            mat[rowCol[0]][rowCol[1]+1] = mat[rowCol[0]][rowCol[1]] + 1
            greedyQueue.append((rowCol[0],rowCol[1]+1))

    return mat


if __name__ == "__main__":
    mat = [[0,0,0],[0,1,0],[1,1,1]]
    print(updateMatrix(mat))