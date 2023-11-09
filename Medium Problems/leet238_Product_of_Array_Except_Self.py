# Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

# You must write an algorithm that runs in O(n) time and without using the division operation.

 

# Example 1:

# Input: nums = [1,2,3,4]
# Output: [24,12,8,6]
# Example 2:

# Input: nums = [-1,1,0,-3,3]
# Output: [0,0,9,0,0]
 

# Constraints:

# 2 <= nums.length <= 105
# -30 <= nums[i] <= 30
# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
 

# Follow up: Can you solve the problem in O(1) extra space complexity? (The output array does not count as extra space for space complexity analysis.)

def productExceptSelf(nums):
 # Best solution from user in JAVA
    res = [1]

    for i in range(1,len(nums)):
        res.append(res[i-1]*nums[i-1])
    
    right = 1
    for i in range(len(nums)-1,-1,-1):
        res[i] *= right
        right *= nums[i]
    
    return res

# Solution implemented with help of hint from question    
    # leftProd = [1]
    # rightProd = [1]
    # res = []

    # for i in range(1,len(nums)):
    #     leftProd.append(leftProd[i-1]*nums[i-1])

    # j = 0
    # for i in range(len(nums)-2,-1,-1):
    #     rightProd.append(rightProd[j]*nums[i+1])
    #     j += 1

    # j = len(nums) - 1

    # for i in range(0,len(nums)):
    #     res.append(leftProd[i] * rightProd[j])
    #     j -= 1

    # return res

if __name__ == "__main__":
    nums = [1,2,3,4]
    print(productExceptSelf(nums))