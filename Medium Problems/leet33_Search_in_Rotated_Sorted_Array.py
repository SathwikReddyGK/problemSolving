def search(nums,target):
    # Implemented Logic2 on my own to understand the corner scenarios
    low = 0
    high = len(nums)-1

    while low<=high:
        mid = (low+high)//2
        num = nums[mid] if ((nums[mid]<nums[0]) == (target<nums[0])) else float("-inf") if target<nums[0] else float("inf")
        
        if num<target:
            low = mid+1
        elif num>target:
            high = mid-1
        else:
            return mid
    
    return -1
    # User Logic 2, converted the java to python and copy pasted
    # Using INF, -INF and ternary operator to the minimum position
    # Approach is, we can see that the first number(nums[0]) is the number where the nums is rotated.
    # So, consider the nums[0] to first smallest element of nums as left half, other half as right half
    # find the position of target and mid. If both are in same half, then it is in sorted half, so
    # follow the normal binary search algorithm. Else, temporarily consider the mid number as 
    # INF(if target is in left half and mid is in right half, since we need to push high to first half)
    # -INF(if target is in right half and mid is in left half, since we need to push low to second half)
    # If we continue this recursively then we will converge to required value
    # lo = 0
    # hi = len(nums)
    # while(lo<hi):
    #     mid = (lo+hi)//2
    #     num = nums[mid] if (nums[mid]<nums[0]) == (target<nums[0]) else float("-inf") if target<nums[0] else float("inf")
    #     if num<target:
    #         lo = mid+1
    #     elif num>target:
    #             hi = mid
    #     else:
    #         return mid
    # return -1

    # User Logic 1
    # Find the low position which gives number of times value is rotated
    # start = 0
    # end = n = len(nums)
    # end = end - 1
    # while start<end:
    #     mid = (start+end)//2

    #     if nums[mid]>nums[end]:
    #         start = mid+1
    #     else:
    #         end = mid
    
    # rot = start
    # start = 0
    # end = n - 1

    # while start<=end:
    #     tempmid = (start+end)//2
    #     mid = (tempmid+rot)%n
    #     if target==nums[mid]:
    #         return mid
    #     elif target>nums[mid]:
    #         start = tempmid+1
    #     else:
    #         end = tempmid-1
    
    # return -1

    

    # First Logic
    # start = 0
    # end = len(nums) - 1
    # n = len(nums)-1

    # while start<=end:
    #     mid = (start+end)//2
        
    #     if target == nums[mid]:
    #         return mid
    #     elif nums[start] <= nums[mid]:
    #         if target>nums[mid] or target<nums[start]:
    #             start = mid+1
    #         else:
    #             end = mid-1
    #     else:
    #         if target<nums[mid] or target>nums[end]:
    #             end = mid-1
    #         else:
    #             start = mid+1

    
    # return -1

if __name__ == "__main__":
    nums = [4,5,6,7,0,1,2]
    target = 0
    print(search(nums,target))