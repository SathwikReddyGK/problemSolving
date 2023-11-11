# Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

 

# Example 1:

# Input: nums = [1,1,1,2,2,3], k = 2
# Output: [1,2]
# Example 2:

# Input: nums = [1], k = 1
# Output: [1]
 

# Constraints:

# 1 <= nums.length <= 105
# -104 <= nums[i] <= 104
# k is in the range [1, the number of unique elements in the array].
# It is guaranteed that the answer is unique.
 

# Follow up: Your algorithm's time complexity must be better than O(n log n), where n is the array's size.
from collections import defaultdict
def topKFrequent(nums,k):
    
    # There are also ways like creating max heap and using Tree to implement this logic
    # not implemented here due to lack of patience for now

    # Below is JAVA code of user converted to python by chatgpt, logic is same as before.
    # This is little faster than what I wrote for same logic
        bucket = [None] * (len(nums) + 1)
        frequency_map = defaultdict(int)

        for n in nums:
            frequency_map[n] += 1

        for key, frequency in frequency_map.items():
            if bucket[frequency] is None:
                bucket[frequency] = []
            bucket[frequency].append(key)

        result = []

        for pos in range(len(bucket) - 1, -1, -1):
            if bucket[pos] is not None:
                result.extend(bucket[pos])
                if len(result) >= k:
                    break

        return result[:k]

    # There was some improvement by using extra list to keep the keys that repeat at position which
    # tells how many times they repeat
    # numsDict = {}
    # res = []
    # tempRes = [[] for _ in range(0,len(nums)+1)]

    # for num in nums:
    #     if num in numsDict:
    #         numsDict[num] += 1
    #     else:
    #         numsDict[num] = 1
    
    # for key,value in numsDict.items():
    #     tempRes[value].append(key)

    # for i in range(len(nums),-1,-1):
    #     if k > 0:
    #         for j in range(0,len(tempRes[i])):
    #             k -= 1
    #             res.append(tempRes[i][j])
    #             if k<=0:
    #                 break
    #     else:
    #         break

    # return res

    # Below is my solution, passed just 5 percent of python users. This can be improved with
    # using one additional list to store values in order of their frequency as shown in above example
    # numsDict = {}
    # res = []

    # for num in nums:
    #     if num in numsDict:
    #         numsDict[num] += 1
    #     else:
    #         numsDict[num] = 1
    
    # for i,value in numsDict.items():
    #     if k>0:
    #         k -= 1
    #         res.append(i)
    #     else:
    #         minVal = float('inf')
    #         minIndex = 0

    #         for j in range(0,len(res)):
    #             if minVal > numsDict[res[j]]:
    #                 minVal = numsDict[res[j]]
    #                 minIndex = j
            
    #         if minVal != 'inf' and minVal < value:
    #             res[minIndex] = i

    # return res

if __name__ == "__main__":
    nums = [1,1,1,2,2,3]
    k = 2
    print(topKFrequent(nums,k))