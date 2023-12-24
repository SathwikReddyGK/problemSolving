# # Description
# Suppose an array of length n sorted in ascending order is rotated between 1 and n times. For example, the array nums = [0,1,2,4,5,6,7] might become:

# [4,5,6,7,0,1,2] if it was rotated 4 times.
# [0,1,2,4,5,6,7] if it was rotated 7 times.
# Notice that rotating an array [a[0], a[1], a[2], ..., a[n-1]] 1 time results in the array [a[n-1], a[0], a[1], a[2], ..., a[n-2]].

# Given the sorted rotated array nums of unique elements, return the minimum element of this array.

# You must write an algorithm that runs in O(log n) time.

 

# Example 1:

# Input: nums = [3,4,5,1,2]
# Output: 1
# Explanation: The original array was [1,2,3,4,5] rotated 3 times.
# Example 2:

# Input: nums = [4,5,6,7,0,1,2]
# Output: 0
# Explanation: The original array was [0,1,2,4,5,6,7] and it was rotated 4 times.
# Example 3:

# Input: nums = [11,13,15,17]
# Output: 11
# Explanation: The original array was [11,13,15,17] and it was rotated 4 times. 
 
# Constraints:

# n == nums.length
# 1 <= n <= 5000
# -5000 <= nums[i] <= 5000
# All the integers of nums are unique.
# nums is sorted and rotated between 1 and n times.

# Solution
# // Time Complexity : O(log(n))
# // Space Complexity : O(1)
# // Did this code successfully run on Leetcode : Yes
# // Any problem you faced while coding this : None


# // Your code here along with comments explaining your approach
# Approach is to understand that if the entire array is sorted, then nums[0]<nums[last], then we can just take nums[0] as answer
# if not then we can apply binary search. Find mid, check if nums[mid]>nums[low], if this is valid then left side of array is sorted
# since the whole array is rotated and left side is sorted, minimum will be in the right side. So we navigate to right side by
# ignoring left side, else we go to left side ignoring the right side. if low and high are equal then we have reached the point
# where we find the lowest number

def findMin(nums):
        # Revisted on 12/23/2023(Implemented the editorial solution)
        start = 0
        end = len(nums)-1

        if nums[start] <= nums[end]:
            return nums[start]

        while start<=end:
            mid = (start+end)//2
            if (nums[mid] < nums[mid-1]):
                return(nums[mid])
            elif nums[mid] > nums[mid+1]:
                return nums[mid+1]
            
            if nums[mid]>=nums[start]:
                start = mid+1
            else:
                end = mid-1
        # neetcode solution implemented
        # start = 0
        # end = len(nums)-1

        # res = nums[0]

        # while start<=end:
        #     if nums[start] <= nums[end]:
        #         res = min(res,nums[start])
        #         break
            
        #     mid = (start+end) // 2
        #     res = min(res,nums[mid])
        #     if nums[mid] >= nums[start]:
        #         start = mid+1
        #     else:
        #         end = mid-1
        
        # return res
        # User Solution1 implemented
        # start = 0
        # end = len(nums) - 1

        # while start<end:
        #     mid = (start+end) // 2

        #     if nums[mid] > nums[end]:
        #         start = mid+1
        #     else:
        #         end = mid
        
        # return nums[start]

if __name__ == "__main__":
     nums = [4,5,6,7,0,1,2]
     print(findMin(nums))