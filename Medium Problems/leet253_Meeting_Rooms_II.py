# Description
# Given an array of meeting time intervals intervals where intervals[i] = [starti, endi], return the minimum number of conference rooms required.

 

# Example 1:

# Input: intervals = [[0,30],[5,10],[15,20]]
# Output: 2
# Example 2:

# Input: intervals = [[7,10],[2,4]]
# Output: 1
 

# Constraints:

# 1 <= intervals.length <= 104
# 0 <= starti < endi <= 106

# Solution

# // Time Complexity : O(NLOGN) since we are sorting the input
# // Space Complexity : O(N) since the heap/priority queue size might be equal to input length
# // Did this code successfully run on Leetcode : Yes 
# // Any problem you faced while coding this : None


# // Your code here along with comments explaining your approach
# Approach is to sort the input. Now add end time of each list into min heap, before adding check if the start time of new
# list is before the end time of min element in heap. If start time is smaller than end time then
# add new end time, else pop old end time and add new end time.
# Take size of queue to find number of rooms
# Basically consider heap/priorirty queue as number of rooms, as you keep adding end time of each meeting into queue, you will
# will be able to figure out when the next meeting will be over. So when you are trying to start a meeting you check if there is
# a meeting getting over before you start new one. Since min heap, least end time will be on the top
from queue import PriorityQueue
def minMeetingRooms(intervals):
    intervals.sort(key = lambda x:x[0])

    rooms = PriorityQueue()

    for interval in intervals:
        if rooms.qsize() > 0:
            temp = rooms.get()
            if interval[0]<temp:
                rooms.put(temp)
            rooms.put(interval[1])
        else:
            rooms.put(interval[1])   

    return rooms.qsize()  

if __name__ == "__main__":
    intervals = [[7,10],[2,4]]
    print(minMeetingRooms(intervals))