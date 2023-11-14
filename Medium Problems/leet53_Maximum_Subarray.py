def maxSubArray(nums):
    
    # As I wrote below solution, since too many edge cases handled separetely wanted to see if there is a better solution, implemented with help fo Sudharshan
    tempSum = nums[0]
    sum = nums[0]
    for i in range(1,len(nums)):  
        tempSum = max(0, tempSum)       
        tempSum += nums[i]     
        
        sum = max(tempSum,sum)    
    return sum
    # My Solution
    # tempSum = nums[0]
    # sum = nums[0]
    # for i in range(1,len(nums)):#num in nums:
    #     if tempSum < 0 and nums[i] < 0 and nums[i] > tempSum:
    #         tempSum = nums[i]
    #     elif tempSum < 0 and nums[i] >= 0:
    #         tempSum = nums[i]
    #     else:
    #         tempSum += nums[i]
        
    #     sum = max(tempSum,sum)
    # sum = max(tempSum,sum)
    # return sum


if __name__ == "__main__":
    nums = [-1,-2,-3]
    print(maxSubArray(nums))