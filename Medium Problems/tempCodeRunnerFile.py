tempSum = nums[0]
    sum = nums[0]
    for i in range(1,len(nums)):  
        tempSum = max(0, tempSum)       
        tempSum += nums[i]     
        
        sum = max(tempSum,sum)    
    return sum