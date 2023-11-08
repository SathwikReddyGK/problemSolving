def maxSubArray(nums):
    i = 0
    j = 1
    sum = nums[i]
    sum2 = sum
    res = 0
    while i<len(nums):
        sum = nums[i]
        sum2 = sum
        while j<len(nums):
            sum2 += nums[j]
            j += 1
            if sum > sum2:
                if res < sum:
                    res = sum
                break
            else:
                sum = sum2
                if res<sum2:
                    res = sum2
        
        i += 1
        j = i+1
    return res

if __name__ == "__main__":
    nums = [-2,1,-3,4,-1,2,1,-5,4]
    print(maxSubArray(nums))