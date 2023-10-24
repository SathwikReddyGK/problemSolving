def majorityElement(nums):
    # Solution 2
    # This works because when we go through the entire array
    # if you consider highest times repeated letter as 1 and all other letters as -1
    # final sum will be positive since highest is greater than n/2, and as the letter change
    # we update that in highest. So finally it should have the highest value
    # This is called Moore Voting Algorithm
    highest = nums[0]
    count = 1
    for i in range(1,len(nums)):
        if count == 0:
            count += 1
            highest = nums[i]
        elif highest == nums[i]:
            count += 1
        else:
            count -= 1
    
    return highest

    # Solution1 by me
    # numsDict = {}
    # for num in nums:
    #     if num in numsDict:
    #         numsDict[num] += 1
    #     else:
    #         numsDict[num] = 1
    
    
    # for key,value in numsDict.items():
    #     if value > (len(nums)/2):
    #         return key

if __name__ == "__main__":
    nums = [2,2,1,2,1,1,2,2]
    print(majorityElement(nums))