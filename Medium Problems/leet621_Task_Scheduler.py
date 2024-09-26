# Solution

# // Time Complexity :  O(N^2)
# // Space Complexity : O(N)
# // Did this code successfully run on Leetcode : Yes
# // Any problem you faced while coding this : No

# // Your code here along with comments explaining your approach
# Greedy Solution - Get the count of each character, should start with highest count so that the idle will be less.
# Use minHeap to always get the highest count(since in python it is always minHeap apply negative sign so that greatest
# gets picked first).
# https://www.youtube.com/watch?v=7ly2mpKEVmo

from collections import Counter
from collections import deque
import heapq

def leastInterval(tasks, n):
    taskCount = Counter(tasks)
    minHeap = [-cnt for cnt in taskCount.values()]
    heapq.heapify(minHeap)
    queue = deque()
    time = 0

    while minHeap or queue:
        time += 1
        
        if minHeap:
            curVal = 1 + heapq.heappop(minHeap)

            if curVal:
                queue.append([curVal,time+n])

        if queue and queue[0][1] == time:
            heapq.heappush(minHeap,queue.popleft()[0])
        
    return time

if __name__ == "__main__":
    tasks = ["A","A","A","B","B","B"]
    n = 2
    print(leastInterval(tasks, n))