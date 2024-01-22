# Description
# There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

# For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
# Return true if you can finish all courses. Otherwise, return false.

 

# Example 1:

# Input: numCourses = 2, prerequisites = [[1,0]]
# Output: true
# Explanation: There are a total of 2 courses to take. 
# To take course 1 you should have finished course 0. So it is possible.
# Example 2:

# Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
# Output: false
# Explanation: There are a total of 2 courses to take. 
# To take course 1 you should have finished course 0, and to take course 0 you should also have finished course 1. So it is impossible.
 

# Constraints:

# 1 <= numCourses <= 2000
# 0 <= prerequisites.length <= 5000
# prerequisites[i].length == 2
# 0 <= ai, bi < numCourses
# All the pairs prerequisites[i] are unique.

# Solution

# // Time Complexity : O(V+E) since we will be removing all the edges one by one to see if all the edges can be removed and
#                      since we do it by going for each vertex once, so we need to include vertex count as well.
# // Space Complexity : O(2V+2E), since dictionary will have all the edges and vertices, indegree will have size equal to number
#                       of vertices and queue size can go upto numbmer of edges in worst case scenario
# // Did this code successfully run on Leetcode : Yes
# // Any problem you faced while coding this : None


# // Your code here along with comments explaining your approach
# Approach is to come up with indegree for all the courses. If as we take courses, indegrees of all courses reduce to zero
# that means we can take all courses. Create a list to hold indegree of each course. Create a adjacency list(using dictionary) for the map/graph which
# keeps track of all the destinations node for each source node, with source node as key of dictonary
# Once these are done, we can find all the vertices with 0 in degree and reduce indegree by one for all the vertices to which 
# current vertex was connected. If any connected vertices's in degree becomes 0, add that to the same queue and further reduce
# indegree for all the connected nodes. Keep a counter to check the number of nodes getting added to queue. If the count is same
# as numCourses once the iteration is done then we can take all courses and we can return True

from collections import deque
def canFinish(numCourses, prerequisites):
        map = {}
        inDegree = [0 for _ in range(0,numCourses)]
        verticesQueue = deque()
        count = 0

        if not prerequisites:
            return True

        for prerequisite in prerequisites:
            out = prerequisite[1]
            to = prerequisite[0]
            if out not in map:
                map[out] = []
            map[out].append(to)
            inDegree[to] += 1
        
        for i in range(0,numCourses):
            if inDegree[i] == 0:
                verticesQueue.append(i)
        
        while verticesQueue:
            count += 1
            vertex = verticesQueue.popleft()
            if vertex in map:
                for out in map[vertex]:
                    inDegree[out] -= 1
                    if inDegree[out] == 0:
                        verticesQueue.append(out)
                
        if count == numCourses:
            return True
        else:
            return False

if __name__ == "__main__":
    # numCourses = 2
    # prerequisites = [[1,0]]
    numCourses = 2
    prerequisites = [[1,0],[0,1]]
    print(canFinish(numCourses,prerequisites))