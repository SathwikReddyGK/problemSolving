def moveZeros(nums):
    slow = 0
    for fast in range(len(nums)):
        if nums[fast] != 0 and nums[slow] == 0:
            nums[fast],nums[slow] = nums[slow],nums[fast]
        
        if nums[slow] != 0:
            slow += 1
    # Solution one with a tad bit improvement
    # i = 0
    # j = 0
    # while j<len(nums):
    #     if nums[j] != 0:
    #         nums[i], nums[j] = nums[j], nums[i]
    #         i += 1
    #         j += 1
    #     else:
    #         j += 1  
    # Solution 1
    # i = 0
    # j = 0
    # while j<len(nums):
    #     if nums[j] != 0 and i != j:
    #         nums[i] ^= nums[j]
    #         nums[j] ^= nums[i]
    #         i += 1
    #         j += 1
    #     elif nums[j] != 0:
    #         i += 1
    #         j += 1
    #     else:
    #         j += 1 
if __name__ == "__main__":
    nums = [0,1,0,3,12]
    moveZeros(nums)
    print(nums)