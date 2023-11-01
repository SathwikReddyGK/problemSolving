import datetime
def subsets(nums):
    # BFS, User logic, trying to implement it
    # As of now I think BFS takes 2^n
    # res = []

    # res.append([])
    # for num in nums:
    #     for i in range(0,len(res)):
    #         res.append(res[i].copy())
    #         res[-1].append(num)
    
    # return res
    # DFS, My solution completed with help of user solution
    # As of now I think DFS takes n!
    res = []
    res.append([])

    def dfs(begin,temp):
        res.append(temp.copy())
        for i in range(begin,len(nums)):
            temp.append(nums[i])
            dfs(i+1,temp)
            temp.pop()
    
    for i in range(0,len(nums)):
        temp = []
        temp.append(nums[i])
        dfs(i+1,temp)
    return res
            
    

if __name__ == "__main__":
    startTime = datetime.datetime.now()
    nums = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
    print(subsets(nums))
    endTime = datetime.datetime.now()
    timeTaken = endTime - startTime
    print("Time Taken:",timeTaken.total_seconds())