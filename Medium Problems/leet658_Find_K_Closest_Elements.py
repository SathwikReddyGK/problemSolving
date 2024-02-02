# Description
# Given a sorted integer array arr, two integers k and x, return the k closest integers to x in the array. The result should also be sorted in ascending order.

# An integer a is closer to x than an integer b if:

# |a - x| < |b - x|, or
# |a - x| == |b - x| and a < b
 

# Example 1:

# Input: arr = [1,2,3,4,5], k = 4, x = 3
# Output: [1,2,3,4]
# Example 2:

# Input: arr = [1,2,3,4,5], k = 4, x = -1
# Output: [1,2,3,4]
 

# Constraints:

# 1 <= k <= arr.length
# 1 <= arr.length <= 104
# arr is sorted in ascending order.
# -104 <= arr[i], x <= 104

# Solution

# // Time Complexity : Modified Binary Search Approach -> O(log(n-k))
#                      Two Pointer Approach: O(N)
# // Space Complexity : Modified Binary Search Approach -> O(1)
#                       Two Pointer Approach: O(1)
# // Did this code successfully run on Leetcode : Yes
# // Any problem you faced while coding this : None


# // Your code here along with comments explaining your approach
# Modified Binary Search Approach: In this approach, we can try to find the start of the range which will be k closest elements
# for X. We start with low = 0 and high = len(arr)-k. Now find mid, let's consider mid as start of the array and check if the
# mid+k element is closer to X or mid is closer to X. (Closer->difference between value and X). If mid is closer, then anything
# after mid cannot be starting element, if mid+k is closer then anything before and equal to mid cannot be the starting point.
# So change low = mid+1 or high = mid based on the conditions. As we keep checking, low and high becomes equal at some point
# giving us the starting index of the result
# 
# Two Pointer Approach: start from first and last of the array, keep checking the distance of each element with X. Whichever is
# bigger move that closer to center. We can do this till the difference between low and high is greater or equal to K. Once
# distance becomes less than k, we have the range and we can take result from that


def findClosestElements(arr, k, x):
    # Two pointer approach(O(n))
    low = 0
    high = len(arr)-1

    while abs(low-high) >= k:
        if abs(arr[low]-x) > abs(arr[high]-x):
            low += 1
        else:
            high -= 1

    result = []
    for i in range(low,low+k):
        result.append(arr[i])

    return result 
    # Below is the best solution
    # low = 0
    # high = len(arr)-k

    # while low<high:
    #     mid = low+((high-low)//2)

    #     sDist = x - arr[mid]
    #     eDist = arr[mid+k] - x

    #     if sDist>eDist:
    #         low = mid+1
    #     else:
    #         high = mid

    # result = []
    # for i in range(low,low+k):
    #     result.append(arr[i])

    # return result 

if __name__ == "__main__":
    arr = [1,2,2,2,2,2,3,50,60]
    k = 3
    x = 3
    print(findClosestElements(arr,k,x))