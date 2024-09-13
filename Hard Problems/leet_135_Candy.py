# Problem

# 135. Candy
# Solved
# Hard
# Topics
# Companies
# There are n children standing in a line. Each child is assigned a rating value given in the integer array ratings.

# You are giving candies to these children subjected to the following requirements:

# Each child must have at least one candy.
# Children with a higher rating get more candies than their neighbors.
# Return the minimum number of candies you need to have to distribute the candies to the children.

 

# Example 1:

# Input: ratings = [1,0,2]
# Output: 5
# Explanation: You can allocate to the first, second and third child with 2, 1, 2 candies respectively.
# Example 2:

# Input: ratings = [1,2,2]
# Output: 4
# Explanation: You can allocate to the first, second and third child with 1, 2, 1 candies respectively.
# The third child gets 1 candy because it satisfies the above two conditions.
 

# Constraints:

# n == ratings.length
# 1 <= n <= 2 * 104
# 0 <= ratings[i] <= 2 * 104

# Solution

# // Time Complexity :  O(N) -> O(2N)
# // Space Complexity : O(N)
# // Did this code successfully run on Leetcode : Yes
# // Any problem you faced while coding this : No

# // Your code here along with comments explaining your approach
# Forward flow to calculate the value based on left number
# Reverse flow to calculate the value based on right number
# https://www.youtube.com/watch?v=GiZevzA0Wn4

def candy(ratings):
    n = len(ratings)
    result = [1]*n
    for i in range(1,n):
        if ratings[i-1] < ratings[i]:
            result[i] = result[i-1] + 1
    
    sum = result[n-1]
    for i in range(n-2,-1,-1):
        if ratings[i+1] < ratings[i]:
            result[i] = max(result[i],result[i+1] + 1)
        
        sum += result[i]
            
    return sum

if __name__ == "__main__":
    ratings = [1,0,2]
    print(candy(ratings))