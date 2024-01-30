# Description
# ou are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.

# Return the number of combinations that make up that amount. If that amount of money cannot be made up by any combination of the coins, return 0.

# You may assume that you have an infinite number of each kind of coin.

# The answer is guaranteed to fit into a signed 32-bit integer.

 

# Example 1:

# Input: amount = 5, coins = [1,2,5]
# Output: 4
# Explanation: there are four ways to make up the amount:
# 5=5
# 5=2+2+1
# 5=2+1+1+1
# 5=1+1+1+1+1
# Example 2:

# Input: amount = 3, coins = [2]
# Output: 0
# Explanation: the amount of 3 cannot be made up just with coins of 2.
# Example 3:

# Input: amount = 10, coins = [10]
# Output: 1
 

# Constraints:

# 1 <= coins.length <= 300
# 1 <= coins[i] <= 5000
# All the values of coins are unique.
# 0 <= amount <= 5000

# Solution

# // Time Complexity : DP Approach: O(m*n) where m is number of coins and n is amount. For each coin we check all the ways we can create
#                      0 to amount, so that we will have solutions for subproblems already
#                      Exhaustive Approach: 2^n, we check all possible paths exhaustively by recursion. Since each element will
#                      have choose/no choose scenario, in worst case we will have 2^n paths/ways to come up with amount.
# // Space Complexity : DP Approach: O(n), since we will have an array which can hold ways to calculate (0,amount) by the previous
#                       coin
#                       Exhaustive Approach: O(L), where L = amount/mincoin, because that is the max height of the tree if we are
#                       looking at choose, no chooose scenario. 
# // Did this code successfully run on Leetcode : Yes
# // Any problem you faced while coding this : None


# // Your code here along with comments explaining your approach
# Put a 2D Array to understand the DP Approach clearly. Rows will be coins. Columns will be 0,1,2,3...amount
# Put 1 for [0,0] and start from there.
# DP Approach: In DP the approach is to remember that we will have overlapping sub problems. So we use an array to hold the 
# number of ways we could get value in the range (0,amount) by the previous coin. When we are working on current coin, the
# number of ways will be, number of ways to get the amount from previous coin + array[value-coin].

# Exhaustive approach: To use recursion to achieve choose, no choose scnearios so that we can find all combinations

# DP with an array for remembering the solution of same overlapping subproblems
def change(amount, coins):
    numberOfWays = [0 for _ in range(amount+1)]
    numberOfWays[0] = 1

    for i in range(len(coins)):
        for j in range(amount+1):
            if j>=coins[i]:
                numberOfWays[j] = numberOfWays[j] + numberOfWays[j-coins[i]]
    
    return numberOfWays[-1]
# Exhaustive approach
# count = 0
#     def change(amount, coins):
#         global count
#         count = 0
#         def helper(amount,coins,idx,sumVal):
#             global count
#             if sumVal == amount:
#                 count += 1
#                 return
            
#             if sumVal > amount or idx>=len(coins):
#                 return

#             helper(amount,coins,idx,sumVal+coins[idx])
#             helper(amount,coins,idx+1,sumVal)
        
#         helper(amount,coins,0,0)
#         return count

if __name__ == "__main__":
    amount = 5
    coins = [1,2,5]
    print(change(amount,coins))