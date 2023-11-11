def threeSum(nums):
    # Two Pointer solution by user, also includes sorting input array first. Implemented from my side
    nums.sort()
    res = []
    for i in range(0,len(nums)):
        if i !=0 and nums[i] == nums[i-1]:
            continue

        target = nums[i]

        front  = i+1
        back = len(nums)-1

        while(front<back):
            if -target > nums[front]+nums[back]:
                front += 1
            elif -target < nums[front]+nums[back]:
                back -= 1
            else:
                res.append([target,nums[front],nums[back]])

                front += 1
                back -= 1
                while(front<back and nums[front] == nums[front-1]):
                    front += 1

                while(front<back and nums[back] == nums[back+1]):
                    back -= 1
    
    return res
        
    # Improvised previous solution, from one of the user solutions got a hint that I can sort the input itself
    # so trying if sorting input would help save time, since I can avoid sorting in loop below and avoid that
    # loop all together
    # This solution got the time down to 1092ms now, which beats 53.33% of python users
    # But space taken is still more, so can reduce using two pointer approach which will be implemented above
    # numDict = {}
    # dupTripList = []
    # tempTripletDict = {}

    # nums.sort()
    # for i in range(0,len(nums)):
    #     numDict[nums[i]] = i

    # listLength = len(nums)

    # for i in range(0,listLength):
    #     if i>0 and nums[i] == nums[i-1]:
    #         continue
    #     for j in range(i+1,listLength):
    #         sum2 = nums[i] + nums[j]

    #         if ( sum2 != 0 and -sum2 in numDict and numDict[-sum2] > i and numDict[-sum2] > j ) or (sum2 == 0 and sum2 in numDict and numDict[sum2] > i and numDict[sum2] > j):
    #             concat = str(nums[i])+str(nums[j])+str(-sum2)
    #             if concat not in tempTripletDict:
    #                 tempTripletDict[concat] = 1
    #                 dupTripList.append([nums[i],nums[j],-sum2])

    # return dupTripList
    # Below is my solution, taking 7154ms, so too much time. I believe it is because of the sort used
    # in the final loop. After reading solutions thought may be we can sort the input to avoid that
    # trying that above
    # numDict = {}
    # dupTripList = []
    # tempTripletDict = {}
    # res = []
    # for i in range(0,len(nums)):
    #     numDict[nums[i]] = i

    # listLength = len(nums)

    # for i in range(0,listLength):
    #     for j in range(i+1,listLength):
    #         sum2 = nums[i] + nums[j]

    #         if ( sum2 != 0 and -sum2 in numDict and numDict[-sum2] > i and numDict[-sum2] != j ) or (sum2 == 0 and sum2 in numDict and numDict[sum2] > i and numDict[sum2] != j):
    #             dupTripList.append([nums[i],nums[j],-sum2])

    # for i in range(0,len(dupTripList)):
    #     dupTripList[i].sort()
    #     concat = str(dupTripList[i][0])+str(dupTripList[i][1])+str(dupTripList[i][2])
    #     if concat not in tempTripletDict:
    #         tempTripletDict[concat] = 1
    #         res.append(dupTripList[i])
    
    # return res

if __name__ == "__main__":
    nums = [1,-1,-1,0]
    print(threeSum(nums))