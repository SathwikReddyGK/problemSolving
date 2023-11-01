def subsets(nums):
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
    nums = [1,2,3,4]
    print(subsets(nums))