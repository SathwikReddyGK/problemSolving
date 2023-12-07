def findMin(nums):
        # neetcode solution implemented
        # start = 0
        # end = len(nums)-1

        # res = nums[0]

        # while start<=end:
        #     if nums[start] <= nums[end]:
        #         res = min(res,nums[start])
        #         break
            
        #     mid = (start+end) // 2
        #     res = min(res,nums[mid])
        #     if nums[mid] >= nums[start]:
        #         start = mid+1
        #     else:
        #         end = mid-1
        
        # return res
        # User Solution1 implemented
        start = 0
        end = len(nums) - 1

        while start<end:
            mid = (start+end) // 2

            if nums[mid] > nums[end]:
                start = mid+1
            else:
                end = mid
        
        return nums[start]

if __name__ == "__main__":
     nums = [4,5,6,7,0,1,2]
     print(findMin(nums))