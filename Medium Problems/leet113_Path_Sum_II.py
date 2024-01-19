# # Description
# Given the root of a binary tree and an integer targetSum, return all root-to-leaf paths where the sum of the node values in the path equals targetSum. Each path should be returned as a list of the node values, not node references.

# A root-to-leaf path is a path starting from the root and ending at any leaf node. A leaf is a node with no children.

 

# Example 1:


# Input: root = [5,4,8,11,null,13,4,7,2,null,null,5,1], targetSum = 22
# Output: [[5,4,11,2],[5,8,4,5]]
# Explanation: There are two paths whose sum equals targetSum:
# 5 + 4 + 11 + 2 = 22
# 5 + 8 + 4 + 5 = 22
# Example 2:


# Input: root = [1,2,3], targetSum = 5
# Output: []
# Example 3:

# Input: root = [1,2], targetSum = 0
# Output: []
 

# Constraints:

# The number of nodes in the tree is in the range [0, 5000].
# -1000 <= Node.val <= 1000
# -1000 <= targetSum <= 1000

# Solution

# // Time Complexity : O(N) since we navigate to all the nodes and check the sum, nothing more
# // Space Complexity : O(H) but since H can be max N in skewed tree we can conside this as O(N). tempPath can be at the max
#                       size of height of tree. Result space can be ignored since we generally ignore result returned space.
#                       Even if considered amortized will be O(N)
# // Did this code successfully run on Leetcode : Yes
# // Any problem you faced while coding this : None


# // Your code here along with comments explaining your approach
# Approach is to recursively navigate into each path of the tree. Take the sum of the path and check if the sum is matching
# the target sum. If matching save that path as list in result. Remember to copy the path into new List
# and BACKTRACK since we are passing by reference.

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

def helper(root,targetSum,curSum,result,tempPath):

    if root == None:
        return
    
    curSum += root.val
    tempPath.append(root.val)

    if root.left == None and root.right == None and curSum == targetSum:
        result.append(tempPath.copy())

    helper(root.left,targetSum,curSum,result,tempPath)
    helper(root.right,targetSum,curSum,result,tempPath)

    # Backtracking
    tempPath.pop()

def pathSum(root, targetSum):
    curSum = 0
    result = []
    tempPath = []
    helper(root,targetSum,curSum,result,tempPath)
    return result

if __name__ == "__main__":
    # Added two more None's since this root creation is done by me and we need to mention None for all the missing
    # binary tree nodes as well.
    ar = [5,4,8,11,None,13,4,7,2,None,None,None,None,5,1]
    n = len(ar)
    root = TreeNode(ar[0],buildLinkedList(1,n),buildLinkedList(2,n))

    targetSum = 22
    print(pathSum(root,targetSum))
