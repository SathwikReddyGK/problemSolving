# Same solution as before, but from user solutions got a hint that I can sort the input itself
    # so trying if sorting input would help save time
    numDict = {}
    dupTripList = []
    tempTripletDict = {}
    res = []

    nums.sort()
    print(nums)
    for i in range(0,len(nums)):
        numDict[nums[i]] = i

    listLength = len(nums)

    for i in range(0,listLength):
        if i>0 and nums[i] == nums[i-1]:
            continue
        for j in range(i+1,listLength):
            sum2 = nums[i] + nums[j]

            if ( sum2 != 0 and -sum2 in numDict and numDict[-sum2] > i and numDict[-sum2] != j ) or (sum2 == 0 and sum2 in numDict and numDict[sum2] > i and numDict[sum2] != j):
                concat = str(nums[i])+str(nums[j])+str(-sum2)
                if concat not in tempTripletDict:
                    tempTripletDict[concat] = 1
                    dupTripList.append([nums[i],nums[j],-sum2])

    print(tempTripletDict)

    # for i in range(0,len(dupTripList)):
    #     dupTripList[i].sort()
    #     concat = str(dupTripList[i][0])+str(dupTripList[i][1])+str(dupTripList[i][2])
    #     if concat not in tempTripletDict:
    #         tempTripletDict[concat] = 1
    #         res.append(dupTripList[i])
    
    return dupTripList