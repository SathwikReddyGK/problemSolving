tempSum = float("inf")
def solution(nums):
    global tempSum
    numList = []
    numLen = len(nums)
    for i in range(numLen-1):
        tempSum = float("inf")
        tempIndex = 0
        for j in range(i+1,numLen-1):
            if nums[i]<nums[j] and nums[i]+nums[j] < tempSum:
                tempSum = nums[i]+nums[j]
                tempIndex = j
        
        if tempSum != float("inf"):
            numList.append([tempIndex,tempSum])

    tempSum = float("inf")
    for elemList in numList:
        for k in range(elemList[0]+1,numLen):
            if nums[elemList[0]] > nums[k] and elemList[1] + nums[k] < tempSum:
                tempSum = elemList[1] + nums[k]
    
    if tempSum == float("inf"):
        return -1
    else:
        return tempSum



    # numLen = len(nums)
    # prevSum = float("inf")

    # for i in range(0,numLen):
    #     for j in range(i+1,numLen):
    #         for k in range(j+1,numLen):
    #             if nums[i]<nums[j] and nums[j] > nums[k]:
    #                 tempSum = nums[i] + nums[j] + nums[k]
    #                 if tempSum < prevSum:
    #                     prevSum = tempSum
    
    # if prevSum == float("inf"):
    #     return -1
    # else:
    #     return prevSum

if __name__ == "__main__":
    nums = [8,6,1,5,3]
    
    # nums = [5,4,8,7,10,2]
    # nums = [6,5,4,3,4,5]
    print(solution(nums))