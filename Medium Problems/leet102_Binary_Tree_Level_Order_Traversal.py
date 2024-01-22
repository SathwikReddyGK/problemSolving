# Description
# Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).

 

# Example 1:


# Input: root = [3,9,20,null,null,15,7]
# Output: [[3],[9,20],[15,7]]
# Example 2:

# Input: root = [1]
# Output: [[1]]
# Example 3:

# Input: root = []
# Output: []
 

# Constraints:

# The number of nodes in the tree is in the range [0, 2000].
# -1000 <= Node.val <= 1000

# Solution

# // Time Complexity : BFS - O(N) since we go through each node
#                      DFS - O(N) since we go through each node
# // Space Complexity : BFS - O(N/2) since at any point of time max size of queue will be the breadth of binary tree and
#                       max breadth of binary tree will be at leaf nodes and max breadth will be N/2
#                       DFS - O(N), it is actually O(H), H is height of binary tree but worst case height will be N
# // Did this code successfully run on Leetcode : Yes
# // Any problem you faced while coding this : None


# // Your code here along with comments explaining your approach
# Approach1 is BFS, we can use a queue to hold the child nodes and then update the current level nodes into a list. Once all
# current level nodes are added in temp list, we can add that list to result. While checking each current level nodes from queue
# we can append child nodes of that node into queue so that those can be processed in next iteration
# Approach2 is DFS, we can keep an empty list as result. Use recursion to go into left and right nodes of each node. As it navigates
# to next level left node, check if list size and level number is same. If same then a list for that level is not in the result list
# so we will add that level list to result list. Now if we go back to previous node and then navigate to the right of the node
# we can see that level is smaller than size of list, so a list already exists in result for that level. So we can access that
# level list using level as the index and add the new element(right element of node) to existing list. 

from collections import deque

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


def levelOrder(root):
    # DFS
    result = []
    def helper(node,level):
        if node == None:
            return
        
        if len(result) == level:
            result.append([])
        
        result[level].append(node.val)
        helper(node.left,level+1)
        helper(node.right,level+1)
    
    helper(root,0)
    return result

    # BFS
    # nodeQueue = deque()
    # prevCount = 1
    # nodeQueue.append(root)
    # result = []

    # while nodeQueue:
    #     curCount = 0
    #     curLevelList = []
    #     while prevCount > 0:
    #         node = nodeQueue.popleft()
    #         prevCount -= 1
    #         if node:
    #             curLevelList.append(node.val)
    #             curCount += 2
    #             nodeQueue.append(node.left)
    #             nodeQueue.append(node.right)
        
    #     if curLevelList:
    #         result.append(curLevelList)
    #     prevCount = curCount
    
    # return result
        

if __name__ == "__main__":
    ar = [3,9,20,None,None,15,7]
    n = len(ar)
    root = TreeNode(ar[0],buildLinkedList(1,n),buildLinkedList(2,n))

    print(levelOrder(root))