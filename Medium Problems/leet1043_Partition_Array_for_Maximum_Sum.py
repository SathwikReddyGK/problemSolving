# Description
# Given an integer array arr, partition the array into (contiguous) subarrays of length at most k. After partitioning, each subarray has their values changed to become the maximum value of that subarray.

# Return the largest sum of the given array after partitioning. Test cases are generated so that the answer fits in a 32-bit integer.

 

# Example 1:

# Input: arr = [1,15,7,9,2,5,10], k = 3
# Output: 84
# Explanation: arr becomes [15,15,15,9,10,10,10]
# Example 2:

# Input: arr = [1,4,1,5,7,3,6,1,9,9,3], k = 4
# Output: 83
# Example 3:

# Input: arr = [1], k = 1
# Output: 1
 

# Constraints:

# 1 <= arr.length <= 500
# 0 <= arr[i] <= 109
# 1 <= k <= arr.length

# Solution

# // Time Complexity : O(k*n) since for each element at the max you go back k steps and calcualte value
# // Space Complexity : O(n) DP array to save the best of the K routes for each element till then
# // Did this code successfully run on Leetcode : Yes
# // Any problem you faced while coding this : None


# // Your code here along with comments explaining your approach
# Use a DP array. For each element we will have K options, either take that element only, or take the max of that and the
# previous element and multiply it twice and so on till, take the max of that element and k-1 elements before that and multiply 
# it K times. So from first element if we follow this approach and keep calculating, if we take just the first element that means
# we have partitioned it there, so rest of the value should be the addition of the best score for the previous element. If we
# take two previous elements, then max(two previous elements)*2 added to the best value for the 3rd previous element.
import math
def maxSumAfterPartitioning(arr,k):
    n = len(arr)
    dp = [-math.inf for _ in range(n)]

    for i in range(n):
        maximum = -math.inf
        for j in range(1,k+1):
            if i-j+1 < 0:
                break
            maximum = max(maximum,arr[i-j+1])
            currval = maximum*j
            if i-j >= 0:
                currval += dp[i-j]
            dp[i] = max(dp[i],currval)
    
    return dp[n-1] 

if __name__ == "__main__":
    arr = [1,15,7,9,2,5,10]
    k = 3
    print(maxSumAfterPartitioning(arr,k))