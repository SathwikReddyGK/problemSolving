# Description
# There is a robot on an m x n grid. The robot is initially located at the top-left corner (i.e., grid[0][0]). The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]). The robot can only move either down or right at any point in time.

# Given the two integers m and n, return the number of possible unique paths that the robot can take to reach the bottom-right corner.

# The test cases are generated so that the answer will be less than or equal to 2 * 109.

 

# Example 1:


# Input: m = 3, n = 7
# Output: 28
# Example 2:

# Input: m = 3, n = 2
# Output: 3
# Explanation: From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
# 1. Right -> Down -> Down
# 2. Down -> Down -> Right
# 3. Down -> Right -> Down
 

# Constraints:

# 1 <= m, n <= 100

# Solution

# // Time Complexity : Exhaustive Time Limit Exceeded approach O(2^(m+n))
#                      DP approach O(m*n)
# // Space Complexity : Exhaustive Time Limit Exceeded approach O(2^(m+n)) implicit recursions
#                       DP approach O(m*n) matrix to hold the values for each input cell
#                       Bit more optimized it will be O(n) n columns
# // Did this code successfully run on Leetcode : Yes
# // Any problem you faced while coding this : None


# // Your code here along with comments explaining your approach
# Approach is for each cell we can either go down or right. Also at each cell number ways to reach the cell is either from up
# or left. So we can keep adding from up and left to get the final result

# # Best solution
def uniquePaths(m,n):
    grid = [1 for _ in range(n)]

    for j in range(1,m):
        for i in range(1,n):
            grid[i] += grid[i-1]

    return grid[n-1]

# 2D Matrix approach, DP with Exhaustive
# def helper(i,j,m,n,dp):
#     if i>m-1 or j>n-1:
#         return 0

#     if dp[i][j] != 0:
#         return dp[i][j]

#     if i == m-1 and j == n-1:
#         return 1
    
#     dp[i][j] = (helper(i+1,j,m,n,dp) + helper(i,j+1,m,n,dp))
#     return dp[i][j]

# def uniquePaths(m, n):
#     dp = [[0 for _ in range(n)] for _ in range(m)]
#     return helper(0,0,m,n,dp)

# Exhaustive Approach
# def uniquePaths(m, n):
#         return helper(0,0,m,n)

# def helper(i,j,m,n):
#     if i>m-1 or j>n-1:
#         return 0

#     if i == m-1 and j == n-1:
#         return 1
    
#     return (helper(i+1,j,m,n) + helper(i,j+1,m,n))

if __name__ == "__main__":
    m = 3
    n = 7
    print(uniquePaths(m,n))