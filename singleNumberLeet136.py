def singleNumber(nums):
    nums.sort()
    result = []
    for num in nums:
        if bool(result) and result[-1] == num:
            result.pop()
        else:
            result.append(num)
    
    return result[0]
if __name__ == "__main__":
    nums = [4,1,2,1,2]
    print(singleNumber(nums))