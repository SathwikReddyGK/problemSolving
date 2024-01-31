# Description
# Given an integer array nums and an integer k, return the kth largest element in the array.

# Note that it is the kth largest element in the sorted order, not the kth distinct element.

# Can you solve it without sorting?

 

# Example 1:

# Input: nums = [3,2,1,5,6,4], k = 2
# Output: 5
# Example 2:

# Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
# Output: 4
 

# Constraints:

# 1 <= k <= nums.length <= 105
# -104 <= nums[i] <= 104

# Solution

# // Time Complexity : Max Heap: O(nlog(n-k+1))
#           Min Heap: O(nlogk) where k is from question. Since we need logk time to add each element in priority queue of size k
# // Space Complexity : Max Heap O(n-k+1)
#                       Min Heap O(k)
# // Did this code successfully run on Leetcode : Yes
# // Any problem you faced while coding this : None

# // Your code here along with comments explaining your approach
# Min Heap Approach(Priority Queue) - Use this if K is small
# Approach is to use Priority Queue of size K. Keep adding all the elements to priority queue. As soon as the size of queue reaches
# k+1, we have k larget elements till now in the bottom and the smallest of the elements added till now on the top of the queue.
# So we can pop the minimum element, we can keep doing that till all the elements are added.Now in queue we will only have the 
# k largest elements and on top will be the kth largest element
# Max Heap Approach(Priority Queue) - Use this if K is large
# we can multiple -1 to each value while inserting. It is still min heap, but since we multiply
# with -1 we can consider it as max heap.
# Max heap will work if we make the queue size as n-k+1. Since we need kth largest and we are using
# max heap, if we save n-k+1 elements and pop any element which is stored in more than n-k+1 position
# in top, we will be removing the top k-1 largest values. So at the end, top of the queue will have
# kth largest element


from queue import PriorityQueue

def findKthLargest(nums, k):
    # Max heap approach
    n = len(nums)
    kthLargest = PriorityQueue(n-k+2)

    for num in nums:
        kthLargest.put((-1*num))
        if kthLargest.qsize() > (n-k+1):
            kthLargest.get()
    
    return (-1*kthLargest.get())
    # Priority Queue approach
    # Time Complexity is O(nlogk) since we take logk time to insert each element. K is because the size
    # of the priority queue is limited to k.
    # Space complexity is O(k) since size of priority queue is k
    # kthLargest = PriorityQueue(k+1)

    # for num in nums:
    #     kthLargest.put(num)
    #     if kthLargest.qsize() > k:
    #         kthLargest.get()
    
    # return kthLargest.get()

if __name__ == "__main__":
    nums = [3,2,1,5,6,4]
    k = 2
    print(findKthLargest(nums, k))