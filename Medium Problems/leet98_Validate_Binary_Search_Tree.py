# Description
# Given the root of a binary tree, determine if it is a valid binary search tree (BST).

# A valid BST is defined as follows:

# The left 
# subtree
#  of a node contains only nodes with keys less than the node's key.
# The right subtree of a node contains only nodes with keys greater than the node's key.
# Both the left and right subtrees must also be binary search trees.
 

# Example 1:


# Input: root = [2,1,3]
# Output: true
# Example 2:


# Input: root = [5,1,4,null,null,3,6]
# Output: false
# Explanation: The root node's value is 5 but its right child's value is 4.
 

# Constraints:

# The number of nodes in the tree is in the range [1, 104].
# -231 <= Node.val <= 231 - 1

# Solution

# // Time Complexity : O(N) since we navigate all nodes to check if BST is valid
# // Space Complexity : O(N) since we are using recursion, there will be stack used to hold recursive calls. It would be
#                       O(H) but H can be N in worst case
# // Did this code successfully run on Leetcode : Yes
# // Any problem you faced while coding this : No


# // Your code here along with comments explaining your approach
# Approach is to use recursion to go to the leftmost node, keeping root node value as Max value. Then perform inorder traversal
# check if left node is smaller than root and then right node is greater than root for each node

# S30 - DFS/Recursion logic

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def recursionRoot(node,mini,maxi):
    if node == None:
        return
    
    if mini != None and node.val <= mini:
        return False
    if maxi != None and node.val >= maxi:
        return False

    if recursionRoot(node.left,mini,node.val) == False:
        return False

    if recursionRoot(node.right,node.val,maxi) == False:
        return False

def buildLinkedList(index,n):
    if index >= n:
        return None
    
    if ar[index] == None:
        return None
    return TreeNode(ar[index],buildLinkedList(index*2 + 1,n),buildLinkedList(index*2 + 2,n))


if __name__ == "__main__":

    ar = [5,1,4,None,None,3,6]
    n = len(ar)
    root = TreeNode(ar[0],buildLinkedList(1,n),buildLinkedList(2,n))


    if recursionRoot(root,None,None) == False:
        print(False)
    else:
        print(True)