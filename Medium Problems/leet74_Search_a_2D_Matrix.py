# # Description
# You are given an m x n integer matrix matrix with the following two properties:

# Each row is sorted in non-decreasing order.
# The first integer of each row is greater than the last integer of the previous row.
# Given an integer target, return true if target is in matrix or false otherwise.

# You must write a solution in O(log(m * n)) time complexity.

 

# Example 1:


# Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
# Output: true
# Example 2:


# Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
# Output: false
 

# Constraints:

# m == matrix.length
# n == matrix[i].length
# 1 <= m, n <= 100
# -104 <= matrix[i][j], target <= 104

# Solution

# // Time Complexity : O(log(m*n))
# // Space Complexity : O(1)
# // Did this code successfully run on Leetcode : Yes
# // Any problem you faced while coding this : None


# // Your code here along with comments explaining your approach
# Approach is to use Binary search to reduce search space. Consider m*n as total number of elements, consider that as high and 0
# as low, find the mid between these two and continue the binary search approach. Logic to convert the mid number to row and
# column is to use modulus and divide. Using modulus of mid with column size helps us bring the mid number back into column range
#  and gives the correct column number. Dividing mid with column number and ceiling it gives us the number of rows needed to
# accomodate that if column size is a certain number thus giving us the row number. Here we are doing floor instead of ceil
# because python matrix is anyways 0 index one

from math import floor
class Solution:
    def searchMatrix(matrix, target):
        # Revisiting on 12/21/2023
        rowSize = len(matrix)
        columnSize = len(matrix[0])

        low = 0
        high = (rowSize*columnSize) - 1

        while low<=high:
            mid = (low+high)//2

            row = floor(mid/columnSize)
            column = mid%columnSize

            if matrix[row][column] == target:
                return True
            elif target>matrix[row][column]:
                low = mid+1
            else:
                high = mid-1
        
        return False


        # rowSize = len(matrix)
        # colSize = len(matrix[0])
        
        # low = 0
        # high = (rowSize*colSize)-1

        # while low<=high:
        #     mid = (low+high)//2

        #     tempRow = mid//(colSize-1)
        #     tempCol = mid%(colSize-1)
        #     if matrix[tempRow][tempCol] == target:
        #         return True
        #     elif matrix[tempRow][tempCol] > target:
        #         low = mid+1
        #     else:
        #         high = mid-1
        
        # return False

        
        # My Solution
        # allElements = []
        # high = 0
        # for m in range(len(matrix)):
        #     for n in range(len(matrix[0])):
        #         allElements.append(matrix[m][n])
        #         high += 1
        
        # low = 0
        # high -= 1
        # mid = 0

        # while low<=high:
        #     mid = (low+high)//2
        #     if allElements[mid] == target:
        #         return True
        #     elif allElements[mid] < target:
        #         low = mid+1
        #     else:
        #         high = mid-1

        # return False

if __name__ == "__main__":
    matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
    target = 3
    print(Solution.searchMatrix(matrix,target))