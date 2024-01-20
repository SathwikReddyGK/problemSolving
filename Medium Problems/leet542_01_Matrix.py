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

# // Time Complexity : O(m*n) since we go through all the elements of matrix to find all zeros
# // Space Complexity : O(m*n) in worst case all the elements can be zero in matrix
# // Did this code successfully run on Leetcode : Yes
# // Any problem you faced while coding this : No


# // Your code here along with comments explaining your approach
# Approach is to first find indices of all the 0's, mark anything with 1 to -1 and add them to queue. Then go through each index in queue and check if there
# are any adjacent cells with -1 then change it to 1 and add indices of that queue. So, once all 0 indices are worked on we will
# have indices of adjacent cells next to cells with 0's. We can call it level 1. We will continue to check if there are still cells
# whose value is -1, if yes then make it 2 and continue

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

        if rowCol[0] > 0 and mat[rowCol[0]-1][rowCol[1]] < 0:
            mat[rowCol[0]-1][rowCol[1]] = mat[rowCol[0]][rowCol[1]] + 1
            greedyQueue.append((rowCol[0]-1,rowCol[1]))
        if rowCol[1] > 0 and mat[rowCol[0]][rowCol[1]-1] < 0:
            mat[rowCol[0]][rowCol[1]-1] = mat[rowCol[0]][rowCol[1]] + 1
            greedyQueue.append((rowCol[0],rowCol[1]-1))
        if rowCol[0]+1 < rowNum and mat[rowCol[0]+1][rowCol[1]] < 0:
             mat[rowCol[0]+1][rowCol[1]] = mat[rowCol[0]][rowCol[1]] + 1
             greedyQueue.append((rowCol[0]+1,rowCol[1]))
        if rowCol[1]+1 < colNum and mat[rowCol[0]][rowCol[1]+1] < 0:
            mat[rowCol[0]][rowCol[1]+1] = mat[rowCol[0]][rowCol[1]] + 1
            greedyQueue.append((rowCol[0],rowCol[1]+1))

    return mat


if __name__ == "__main__":
    mat = [[0,1,0,1,1],[1,1,0,0,1],[0,0,0,1,0],[1,0,1,1,1],[1,0,0,0,1]]
    # expected
    # [[0,1,0,1,2],[1,1,0,0,1],[0,0,0,1,0],[1,0,1,1,1],[1,0,0,0,1]]
    print(updateMatrix(mat))