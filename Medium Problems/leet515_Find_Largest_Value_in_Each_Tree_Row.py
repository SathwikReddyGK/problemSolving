# Description
# Given the root of a binary tree, return an array of the largest value in each row of the tree (0-indexed).

 

# Example 1:


# Input: root = [1,3,2,5,3,null,9]
# Output: [1,3,9]
# Example 2:

# Input: root = [1,2,3]
# Output: [1,3]
 

# Constraints:

# The number of nodes in the tree will be in the range [0, 104].
# -231 <= Node.val <= 231 - 1

# Solution

# // Time Complexity : O(N) since we will be iterating over all the nodes of Binary tree
# // Space Complexity : O(N/2) since in worst case all the leaf nodes will be in queue, number of leaf nodes will be N/2
# // Did this code successfully run on Leetcode : Yes
# // Any problem you faced while coding this : None


# // Your code here along with comments explaining your approach
# Approach is to perform level order traversal using BFS and keep a check on the highest level number in each level and append
# that to result list

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def buildLinkedList(index,n):
    if index >= n:
        return None
    
    if ar[index] == None:
        return None
    return TreeNode(ar[index],buildLinkedList(index*2 + 1,n),buildLinkedList(index*2 + 2,n))


from collections import deque
import math
def largestValues(root):
    # BFS
    nodeQueue = deque()
    nodeQueue.append(root)
    prevCount = 1
    curCount = 0
    result = []

    while nodeQueue:
        levelMax = -math.inf
        curCount = 0
        while prevCount > 0:
            node = nodeQueue.popleft()
            if node == None:
                prevCount -= 1
                continue
            levelMax = max(levelMax,node.val)
            prevCount -= 1
            if node.left != None:
                nodeQueue.append(node.left)
                curCount += 1
            
            if node.right != None:
                nodeQueue.append(node.right)
                curCount += 1
        
        if levelMax != -math.inf:
            result.append(levelMax)
        prevCount = curCount
    
    return result

if __name__ == "__main__":
    ar = [1,3,2,5,3,None,9]
    n = len(ar)
    root = TreeNode(ar[0],buildLinkedList(1,n),buildLinkedList(2,n))
    print(largestValues(root))