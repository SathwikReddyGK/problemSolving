# Problem
# 739. Daily Temperatures
# Solved
# Medium
# Topics
# Companies
# Hint
# Given an array of integers temperatures represents the daily temperatures, return an array answer such that answer[i] is the number of days you have to wait after the ith day to get a warmer temperature. If there is no future day for which this is possible, keep answer[i] == 0 instead.

 

# Example 1:

# Input: temperatures = [73,74,75,71,69,72,76,73]
# Output: [1,1,4,2,1,1,0,0]
# Example 2:

# Input: temperatures = [30,40,50,60]
# Output: [1,1,1,0]
# Example 3:

# Input: temperatures = [30,60,90]
# Output: [1,1,0]
 

# Constraints:

# 1 <= temperatures.length <= 105
# 30 <= temperatures[i] <= 100

# Solution

# // Time Complexity :  O(2N)
# // Space Complexity : O(N)
# // Did this code successfully run on Leetcode : Yes
# // Any problem you faced while coding this : No

# // Your code here along with comments explaining your approach
# Monotonic Stack to maintain entries in ascending order and keep checking new entries
# or indexes while going through loop
# https://www.youtube.com/watch?v=Es_eNOlpqEQ

from collections import deque

def dailyTemperatures(temperatures):
    n = len(temperatures)
    queue = deque()
    result = [0]*n

    for i in range(0,n):
        if len(queue) > 0:
            if temperatures[i] > temperatures[queue[-1]]:
                while len(queue) > 0 and temperatures[i] > temperatures[queue[-1]]:
                    tempIdx = queue.pop()
                    result[tempIdx] = i - tempIdx
        
        queue.append(i)
    
    return result

if __name__ == "__main__":
    temperatures = [73,74,75,71,69,72,76,73]
    print(dailyTemperatures(temperatures))