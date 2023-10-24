import functools
def containsDuplicate(nums):
    # User solution, using all() function, saves memory but takes time compared to other solutions
    nums.sort()
    for i in range(len(nums)-1):
        nums[i] -= nums[i+1]
    
    return len(nums)>1 and not all(nums)
    # User Solution, improvisation of set solution
    # numSet = set()
    # for num in nums:
    #     if num in numSet:
    #         return True
    #     else:
    #         numSet.add(num)
    
    # return False
    # Going with normal dictionary method to test the time
    # numDict = {}
    # for num in nums:
    #     if num in numDict:
    #         numDict[num] += 1
    #     else:
    #         numDict[num] = 1
    
    # for value in numDict.values():
    #     if value > 1:
    #         return True
    
    # return False
    # print(list(functools.reduce(lambda test,num2,num3: num2 if num3>1 else False,numDict)))

    # User solution, took more than sets around 523ms
    # nums.sort()
    # for i in range(len(nums)-1):
    #     if nums[i] == nums[i+1]:
    #         return True
    
    # return False
    # My solution Using set since sets always will have unique values, took 500ms
    # numset = set(nums)

    # if len(numset) == len(nums):
    #     return False
    # else:
    #     return True
        

if __name__ == "__main__":
    nums = [1,2,3,1]
    print(containsDuplicate(nums))