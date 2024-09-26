# Problem
# 406. Queue Reconstruction by Height
# Medium
# Topics
# Companies
# Hint
# You are given an array of people, people, which are the attributes of some people in a queue (not necessarily in order). Each people[i] = [hi, ki] represents the ith person of height hi with exactly ki other people in front who have a height greater than or equal to hi.

# Reconstruct and return the queue that is represented by the input array people. The returned queue should be formatted as an array queue, where queue[j] = [hj, kj] is the attributes of the jth person in the queue (queue[0] is the person at the front of the queue).

 

# Example 1:

# Input: people = [[7,0],[4,4],[7,1],[5,0],[6,1],[5,2]]
# Output: [[5,0],[7,0],[5,2],[6,1],[4,4],[7,1]]
# Explanation:
# Person 0 has height 5 with no other people taller or the same height in front.
# Person 1 has height 7 with no other people taller or the same height in front.
# Person 2 has height 5 with two persons taller or the same height in front, which is person 0 and 1.
# Person 3 has height 6 with one person taller or the same height in front, which is person 1.
# Person 4 has height 4 with four people taller or the same height in front, which are people 0, 1, 2, and 3.
# Person 5 has height 7 with one person taller or the same height in front, which is person 1.
# Hence [[5,0],[7,0],[5,2],[6,1],[4,4],[7,1]] is the reconstructed queue.
# Example 2:

# Input: people = [[6,0],[5,0],[4,0],[3,2],[2,2],[1,4]]
# Output: [[4,0],[5,0],[2,2],[3,2],[1,4],[6,0]]
 

# Constraints:

# 1 <= people.length <= 2000
# 0 <= hi <= 106
# 0 <= ki < people.length
# It is guaranteed that the queue can be reconstructed.

# Solution

# // Time Complexity :  O(N^2)
# // Space Complexity : O(N)
# // Did this code successfully run on Leetcode : Yes
# // Any problem you faced while coding this : No

# // Your code here along with comments explaining your approach
# Greedy Solution - Sort acending the queue based on height and if height is same then sort acending on number of people
# ahead. Now just putting each in the respective indexs should work, since adding smaller heights elements infront of 
# larger heights elements.
# https://www.youtube.com/watch?v=7ly2mpKEVmo

from collections import deque
from functools import cmp_to_key

def compare(item1,item2):
        if item1[0] < item2[0]:
            return 1
        elif item1[0] == item2[0]:
            if item1[1] > item2[1]:
                return 1

        return -1

def reconstructQueue(people):
    peopleSort = sorted(people, key=cmp_to_key(compare))
    queue = deque()
    result = []

    for peeps in peopleSort:
        queue.insert(peeps[1],peeps)
    
    while queue:
        result.append(queue.popleft())
    
    return result

if __name__ == "__main__":
    people = [[7,0],[4,4],[7,1],[5,0],[6,1],[5,2]] 
    print(reconstructQueue(people))