# Solution

# // Time Complexity :  O(3N) -> Worst case when none of the values have higher value till the last element
# // Space Complexity : O(N)
# // Did this code successfully run on Leetcode : Yes
# // Any problem you faced while coding this : No

# // Your code here along with comments explaining your approach
# Monotonic Stack to maintain entries in ascending order and keep checking new entries
# or indexes while going through loop. Also have one more loop where we only process the entries that were not processed
# and are part of queue, to check if there were any elements on the left side of the number which were greater since array
# is cyclical
# https://www.youtube.com/watch?v=Es_eNOlpqEQ

from collections import deque
def nextGreaterElements(nums):
    monotonic = deque()
    n = len(nums)
    result = [-1]*n

    for i in range(n):
        if len(monotonic) > 0:
            if nums[i] > nums[monotonic[-1]]:
                while len(monotonic) > 0 and nums[i] > nums[monotonic[-1]]:
                    idx = monotonic.pop()
                    result[idx] = nums[i]
        
        monotonic.append(i)
    
    end = monotonic[-1]
    print(monotonic)
    if len(monotonic) > 0:
        for i in range(end):
            if len(monotonic) > 0:
                if nums[i] > nums[monotonic[-1]]:
                    while len(monotonic) > 0 and nums[i] > nums[monotonic[-1]]:
                        idx = monotonic.pop()
                        result[idx] = nums[i]
    
    return result

if __name__ == "__main__":
    nums = [1,2,3,4,3]
    print(nextGreaterElements(nums))