def maxSubArray(nums):
    tempSum = 0
    for num in nums:
        if tempSum < 0 and num < 0 and num > tempSum:
            tempSum = num
        elif tempSum < 0 and num >= 0:
            tempSum = num
        else:
            tempSum += num
    
    return tempSum


if __name__ == "__main__":
    nums = [-2,1,-3,4,-1,2,1,-5,4]
    print(maxSubArray(nums))