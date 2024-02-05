# Given an n x n matrix where each of the rows and columns is sorted in ascending order, return the kth smallest element in the matrix.

# Note that it is the kth smallest element in the sorted order, not the kth distinct element.

# You must find a solution with a memory complexity better than O(n2).

 

# Example 1:

# Input: matrix = [[1,5,9],[10,11,13],[12,13,15]], k = 8
# Output: 13
# Explanation: The elements in the matrix are [1,5,9,10,11,12,13,13,15], and the 8th smallest number is 13
# Example 2:

# Input: matrix = [[-5]], k = 1
# Output: -5
 

# Constraints:

# n == matrix.length == matrix[i].length
# 1 <= n <= 300
# -109 <= matrix[i][j] <= 109
# All the rows and columns of matrix are guaranteed to be sorted in non-decreasing order.
# 1 <= k <= n2
 

# Follow up:

# Could you solve the problem with a constant memory (i.e., O(1) memory complexity)?
# Could you solve the problem in O(n) time complexity? The solution may be too advanced for an interview but you may find reading this paper fun.

# Solution

# // Time Complexity : Min Heap Approach: O(KLOGN) where N is the number of rows
#                      Binary Search Approach: O(NLOG(MAX-MIN)) where N is to find the count of numbers less than 
#                      mid(and find next range to be used) and LOG(MAX-MIN) gives the time complexity for Binary Search. Where
#                      MAX is the maximum element(matrix[n-1][n-1]) of matrix and MIN is the minimum element of matrix(matrix[0][0])
# // Space Complexity : Min Heap Approach: O(N)
#                       Binary Search Approach: O(1)
# // Did this code successfully run on Leetcode : Yes
# // Any problem you faced while coding this : None


# // Your code here along with comments explaining your approach
# Minheap Approach: We can consider each row of matrix as a list. So we will have N Lists. Now we can use approach similar to
# two pointer when we are trying to merge two sorted arrays. Only thing is, we use min heap as data structure which can hold
# pointers for each list. So we add first elements of each list into min heap. Now we pop the min out and add the next element of
# that list. If we do this K times, the Kth element which gets popped will be the Kth smallest element.
# Binary Search Approach: We can take first element of matrix as "low" and last element of matrix as "high", since these elements
# are the smallest and largest in the entire matrix. Now we can find mid between these two values. And check the number of
# elements in matrix which are smaller than or equal to the mid.
# To find count of smaller or equal elements: We should start from the bottom row and first column. If we find a value smaller than
# mid that means all other values above and including that in that column will be less than mid. So if "i" is the row number then
# we can add i+1 to count(since i is 0 index approach). Once we find this, we can increment the column to check if the value is
# smaller again or not. If smaller again add the count else, decrement the row till you find a value smaller. If found again
# increment the column and do this till we cover all the elements smaller than mid. While doing this, we also need to find the
# minimum(we can call it MIN) from the elements larger than mid and maximum(we can call it MAX) from the elements smaller than mid.
#  This will be used to set the new range between which we will have to find the kth smallest element again. MIN will be used as
# "high" if count > k so that we can reduce the scope, MAX will be used as "low" if count<k so that we can increase the scope
# to find the right mid. If count == mid then we will have the kth smallest element in MAX, if low<high breaks then low will have
# the result

from queue import PriorityQueue
import math

def countLessOrEqual(n,matrix,mid):
    row = n-1
    col = 0
    count = 0
    smaller = math.inf
    larger = -math.inf
    while row<n and col<n and row>=0 and col>=0:
        if matrix[row][col] > mid:
            smaller = min(smaller,matrix[row][col])
            row -= 1
        else:
            larger = max(larger,matrix[row][col])
            col += 1
            count += row+1
    
    return smaller,larger,count

def kthSmallest(matrix, k):
    # O()
    n = len(matrix)
    low = matrix[0][0]
    high = matrix[n-1][n-1] 

    while low<high:
        mid = low+((high-low)//2)
        smaller,larger,count = countLessOrEqual(n,matrix,mid)

        if count<k:
            low = smaller
        elif count>k:
            high = larger
        else:
            return larger
    
    return low
    # O(KLOGN) space is O(N)
    # n = len(matrix)
    # count = 0
    # listPointers = PriorityQueue(n)
    # for i in range(n):
    #     listPointers.put((matrix[i][0],count,[i,0]))
    #     count += 1
    
    # result = 0
    # while k>0:
    #     result = listPointers.get()
    #     k -= 1
    #     newRow = result[2][0]
    #     newCol = result[2][1]+1
    #     if newRow<n and newCol<n:
    #         listPointers.put((matrix[newRow][newCol],count,[newRow,newCol]))
    #         count += 1
    
    # return result[0]

if __name__ == "__main__":
    matrix = [[1,5,9],[10,11,13],[12,13,15]]
    k = 8
    print(kthSmallest(matrix, k))