def helper(nums,pivot,path,result):
        for i in range(pivot,len(nums)):
            path.append(nums[i])
            result.append(path.copy())
            helper(nums,i+1,path,result)
            path.pop()
    result = [[]]
    helper(nums,0,[],result)
    return result