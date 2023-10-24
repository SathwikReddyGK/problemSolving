def missingNumber(nums):
    # User solution 3, similar to mine with better syntax
    length = len(nums)
    return ((length*(length + 1))//2) - sum(nums)
    # User Solution 2
    # nums.sort()
    # left = 0
    # right = len(nums)

    # while left<right:
    #     mid = (left+right)//2

    #     if nums[mid]>mid:
    #         right = mid
    #     else:
    #         left = mid+1

    # return left

    # User Solution
    # xor = 0
    # # This is because XOR with same number gives zero, so xoring all the values with index
    # # should ideally give 0, so missing index xored with 0 gives missing number
    # for i in range(0,len(nums)):
    #     xor ^= i ^ nums[i]
    
    # xor ^= len(nums)
    # return xor
    # My Solution
    # length = len(nums)
    # sum = length*(length+1)//2
    # numSum = 0

    # for c in nums:
    #     numSum += c
    
    # return sum - numSum
if __name__ == "__main__":
    nums = [3,0,1]
    print(missingNumber(nums))