# Description
# Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.

# According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”

 

# Example 1:


# Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
# Output: 3
# Explanation: The LCA of nodes 5 and 1 is 3.
# Example 2:


# Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
# Output: 5
# Explanation: The LCA of nodes 5 and 4 is 5, since a node can be a descendant of itself according to the LCA definition.
# Example 3:

# Input: root = [1,2], p = 1, q = 2
# Output: 1
 

# Constraints:

# The number of nodes in the tree is in the range [2, 105].
# -109 <= Node.val <= 109
# All Node.val are unique.
# p != q
# p and q will exist in the tree.

# Solution

# // Time Complexity : Second Approach O(n)  we might end up looking at all the nodes
#                       First Approach O(n) we might end up looking at all the nodes
# // Space Complexity : Second Approach O(1) we are not 
#                       First Approach O(n) since we will be using list to save paths 
# // Did this code successfully run on Leetcode : Yes
# // Any problem you faced while coding this : None


# // Your code here along with comments explaining your approach
# DFS should be done and we need to keep recording the path we are travelling, when we reach one of the numbers either p or q
# we should record the path we travelled. Once we save both paths related to p and q, last element which is common between both
# paths will be the result node

# This does not run since I have not worked on creating the BST part instead just wrote the solution

def lowestCommonAncestor(root,p,q):
    left = None
    right = None
    if root == None or root.val == p.val or root.val == q.val:
        return root
    
    left = lowestCommonAncestor(root.left,p,q)
    right = lowestCommonAncestor(root.right,p,q)

    if left == None and right == None:
        return None
    elif left != None and right == None:
        return left
    elif left == None and right != None:
        return right
    else:
        return root

# def lowestCommonAncestor(root,p,q):
#     pathP = []
#     pathQ = []
#     if p.val == root.val or q.val == root.val:
#         return root
    
#     helper(root,p,q,[],pathP,pathQ)
#     n = min(len(pathP[0]),len(pathQ[0]))
#     for i in range(0,n):
#         nodeP = pathP[0][i]
#         nodeQ = pathQ[0][i]
#         if nodeP != nodeQ:
#             return pathP[0][i-1]
    
#     return None
    
# def helper(root,p,q,path,pathP,pathQ):
#     if root == None:
#         return
#     path.append(root)
#     if root.val == p.val:
#         path.append(root)
#         pathP.append(path.copy())
#         path.pop()
        
#     if root.val == q.val:
#         path.append(root)
#         pathQ.append(path.copy())
#         path.pop()
    
#     helper(root.left,p,q,path,pathP,pathQ)
#     helper(root.right,p,q,path,pathP,pathQ)
#     path.pop()