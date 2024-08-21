# Description
# Given the root of a binary search tree, return a balanced binary search tree with the same node values. If there is more than one answer, return any of them.

# A binary search tree is balanced if the depth of the two subtrees of every node never differs by more than 1.

 

# Example 1:


# Input: root = [1,null,2,null,3,null,4,null,null]
# Output: [2,1,3,null,null,null,4]
# Explanation: This is not the only correct answer, [3,1,4,null,2] is also correct.
# Example 2:


# Input: root = [2,1,3]
# Output: [2,1,3]
 

# Constraints:

# The number of nodes in the tree is in the range [1, 104].
# 1 <= Node.val <= 105

# Solution

# // Time Complexity : O(N) where N is number of nodes
# // Space Complexity : O(N) array used to save the values in order
# // Did this code successfully run on Leetcode : Yes
# // Any problem you faced while coding this : None


# // Your code here along with comments explaining your approach
# Save all the node values by traversing in-order, into an array. We should build balanced BST using this array.
# Now by finding the mid of array, make that the root. Recursively perform this mid calculation for the left half to find 
# the left node of the root and right half for the right root

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def helper(self,root,arr):
        if root == None:
            return
        
        self.helper(root.left,arr)
        arr.append(root.val)
        self.helper(root.right,arr)

    def buildBST(self,start,end,arr):
        if start>end:
            return None
        
        mid = (start+end)//2

        root = TreeNode(arr[mid])
        root.left = self.buildBST(start,mid-1,arr)
        root.right = self.buildBST(mid+1,end,arr)
        
        return root

    def balanceBST(self, root: TreeNode) -> TreeNode:
        arr = []

        self.helper(root,arr)
        return self.buildBST(0,len(arr)-1,arr)

