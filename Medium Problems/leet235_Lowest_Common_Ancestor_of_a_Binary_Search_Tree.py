# Description
# Given a binary search tree (BST), find the lowest common ancestor (LCA) node of two given nodes in the BST.

# According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”

 

# Example 1:


# Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 8
# Output: 6
# Explanation: The LCA of nodes 2 and 8 is 6.
# Example 2:


# Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 4
# Output: 2
# Explanation: The LCA of nodes 2 and 4 is 2, since a node can be a descendant of itself according to the LCA definition.
# Example 3:

# Input: root = [2,1], p = 2, q = 1
# Output: 2
 

# Constraints:

# The number of nodes in the tree is in the range [2, 105].
# -109 <= Node.val <= 109
# All Node.val are unique.
# p != q
# p and q will exist in the BST.

# Solution

# // Time Complexity : O(log(h)) h is the height of the tree
# // Space Complexity : O(1) 
# // Did this code successfully run on Leetcode : Yes
# // Any problem you faced while coding this : None


# // Your code here along with comments explaining your approach
# Since this is a BST, if both p and q are greater than root then the common ancestor will be on the right side of the tree
# if both p and q are lesser than root then the common ancestor will be on the left side of the tree, if each one of them are
# on the either side of the root, that means root is the least common ancestor. If either p or q is the root then whichever is
# the root is the least common ancestor

# This does not run since I have not worked on creating the BST part instead just wrote the solution

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def lowestCommonAncestor(root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
    while root:
        if p.val>root.val and q.val>root.val:
            root = root.right
        elif p.val<root.val and q.val<root.val:
            root = root.left
        elif (p.val == root.val) or (q.val == root.val) or (p.val<root.val and q.val>root.val) or (p.val>root.val and q.val<root.val):
            return root