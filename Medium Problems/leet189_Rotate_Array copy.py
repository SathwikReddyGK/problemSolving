# Problem
# 189. Rotate Array
# Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.
# 
# Example 1:
# Input: nums = [1,2,3,4,5,6,7], k = 3
# Output: [5,6,7,1,2,3,4]
# Explanation:
# rotate 1 steps to the right: [7,1,2,3,4,5,6]
# rotate 2 steps to the right: [6,7,1,2,3,4,5]
# rotate 3 steps to the right: [5,6,7,1,2,3,4]
# 
# Example 2:
# Input: nums = [-1,-100,3,99], k = 2
# Output: [3,99,-1,-100]
# Explanation: 
# rotate 1 steps to the right: [99,-1,-100,3]
# rotate 2 steps to the right: [3,99,-1,-100]
 

# Constraints:

# 1 <= nums.length <= 105
# -231 <= nums[i] <= 231 - 1
# 0 <= k <= 105
 

# Follow up:

# Try to come up with as many solutions as you can. There are at least three different ways to solve this problem.
# Could you do it in-place with O(1) extra space?

# Solution

# // Time Complexity : Brute Force - O(N*K)
#                      Optimized Approach - O(N)
# // Space Complexity : O(1)
# // Did this code successfully run on Leetcode : Yes
# // Any problem you faced while coding this : No

# // Your code here along with comments explaining your approach
# Optimized approach is to reverse the array and then reverse the first K elements and last n-k elements
# https://www.youtube.com/watch?v=ZEjyrZgNdJQ

def reverse(start,end,arr):
        while end>start:
            newVal = arr[end]
            arr[end] = arr[start]
            arr[start] = newVal

            start += 1
            end -= 1

def rotate(nums, k):
    """
    Do not return anything, modify nums in-place instead.
    """
    n = len(nums)
    times = k%n

    if times != n:
        reverse(0,n-1,nums)
        reverse(0,times-1,nums)
        reverse(times,n-1,nums)

# Bruteforce
# n = len(nums)
# times = k%n
# while times>0:
#     times -= 1

#     i = 0
#     oldVal = nums[0]

#     while i<n-1:
#         i += 1
#         newVal = nums[i]
#         nums[i] = oldVal
#         oldVal = newVal
    
#     nums[0] = oldVal

if __name__ == "__main__":
     nums = [1,2,3,4,5,6,7]
     k = 3
     rotate(nums, k)
     print(nums)