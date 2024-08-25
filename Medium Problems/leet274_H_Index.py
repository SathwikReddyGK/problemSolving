# Problem
# 274. H-Index
# Medium
# Topics
# Companies
# Hint
# Given an array of integers citations where citations[i] is the number of citations a researcher received for their ith paper, return the researcher's h-index.

# According to the definition of h-index on Wikipedia: The h-index is defined as the maximum value of h such that the given researcher has published at least h papers that have each been cited at least h times.

 

# Example 1:

# Input: citations = [3,0,6,1,5]
# Output: 3
# Explanation: [3,0,6,1,5] means the researcher has 5 papers in total and each of them had received 3, 0, 6, 1, 5 citations respectively.
# Since the researcher has 3 papers with at least 3 citations each and the remaining two with no more than 3 citations each, their h-index is 3.
# Example 2:

# Input: citations = [1,3,1]
# Output: 1
 

# Constraints:

# n == citations.length
# 1 <= n <= 5000
# 0 <= citations[i] <= 1000
# Solution

# // Time Complexity : O(N)
# // Space Complexity : O(N) - Array
# // Did this code successfully run on Leetcode : Yes
# // Any problem you faced while coding this : No

# // Your code here along with comments explaining your approach
# Approach is using buckets to hold number of papers with citations, find more in below link
# https://www.youtube.com/watch?v=ZEjyrZgNdJQ

def hIndex(citations):
    n = len(citations)

    arr = [0]*(n+1)

    for elem in citations:
        if elem >= n:
            arr[n] += 1
        else:
            arr[elem] += 1
    
    sum = 0
    for i in range(n,-1,-1):
        sum += arr[i]
        if sum >= i:
            return i

if __name__ == "__main__":
    citations = [3,0,6,1,5]
    # citations = [1,3,1]
    print(hIndex(citations))