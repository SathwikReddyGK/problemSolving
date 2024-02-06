# Description
# You are given all the nodes of an N-ary tree as an array of Node objects, where each node has a unique value.

# Return the root of the N-ary tree.

# Custom testing:

# An N-ary tree can be serialized as represented in its level order traversal where each group of children is separated by the null value (see examples).



# For example, the above tree is serialized as [1,null,2,3,4,5,null,null,6,7,null,8,null,9,10,null,null,11,null,12,null,13,null,null,14].

# The testing will be done in the following way:

# The input data should be provided as a serialization of the tree.
# The driver code will construct the tree from the serialized input data and put each Node object into an array in an arbitrary order.
# The driver code will pass the array to findRoot, and your function should find and return the root Node object in the array.
# The driver code will take the returned Node object and serialize it. If the serialized value and the input data are the same, the test passes.
 

# Example 1:



# Input: tree = [1,null,3,2,4,null,5,6]
# Output: [1,null,3,2,4,null,5,6]
# Explanation: The tree from the input data is shown above.
# The driver code creates the tree and gives findRoot the Node objects in an arbitrary order.
# For example, the passed array could be [Node(5),Node(4),Node(3),Node(6),Node(2),Node(1)] or [Node(2),Node(6),Node(1),Node(3),Node(5),Node(4)].
# The findRoot function should return the root Node(1), and the driver code will serialize it and compare with the input data.
# The input data and serialized Node(1) are the same, so the test passes.
# Example 2:



# Input: tree = [1,null,2,3,4,5,null,null,6,7,null,8,null,9,10,null,null,11,null,12,null,13,null,null,14]
# Output: [1,null,2,3,4,5,null,null,6,7,null,8,null,9,10,null,null,11,null,12,null,13,null,null,14]
 

# Constraints:

# The total number of nodes is between [1, 5 * 104].
# Each node has a unique value.
 

# Follow up:

# Could you solve this problem in constant space complexity with a linear time algorithm?

# Solution

# // Time Complexity : Brute Force, SUM and XOR Approach: O(N)
# // Space Complexity : Brute Force Approach: O(N)
#                       SUM and XOR Approach: O(1)
# // Did this code successfully run on Leetcode : Yes
# // Any problem you faced while coding this : None


# // Your code here along with comments explaining your approach
# Bruteforce Approach: We go to each node and put the children into a set. As we are going on with each and every node, once we are done with everything there will be one node value missing in children. That will be the
# root node.
# SUM and XOR Approach: We iterate on each node, and perform a SUM or XOR on the node val and then perform SUBTRACT or XOR on that node's children. Since we are subtracting all the children from all the parent node values,
# the final value remaining in the variable used to SUM or XOR will have the root node value. Now we can just iterate over the entire nodes again till we find the node with that value.
# 	XOR
# 	A XOR A = 0
# 	0 XOR A = A
	
# 	1 XOR 1 = 0
# 	0 XOR 0 = 0 
# 	0 XOR 1 = 1 
#   1 XOR 0 = 1

# This code will not run here because of the way leetcode is checking the answers. Did not try to replicate that here

"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []
"""

class Solution:
    def findRoot(self, tree: List['Node']) -> 'Node':
        # Same solution as the previous one, but we will consider XOR instead of sum and subtract
        # Time Complexity O(N) actually O(3N)
        # Space Complexity O(1)
        sum = 0
        for node in tree:
            sum ^= node.val
            for child in node.children:
                sum ^= child.val
        
        for node in tree:
            if sum == node.val:
                return node
        # Time Complexity O(N) actually O(3N)
        # Space Complexity O(1)
        # sum = 0
        # for node in tree:
        #     sum += node.val
        #     for child in node.children:
        #         sum -= child.val
        
        # for node in tree:
        #     if sum == node.val:
        #         return node
        # Time Complexity: O(N)
        # Space Complexity: O(N)
        # parentDict = {}
        # childDict = set()
        # for nodes in tree:
        #     print(nodes.val)
        # for node in tree:
        #     if node.val in childDict:
        #         if node.val in parentDict:
        #             del parentDict[node.val]
        #         for childNode in node.children:
        #             childDict.add(childNode.val)
        #             if childNode.val in parentDict:
        #                 del parentDict[childNode.val]
        #     else:
        #         parentDict[node.val] = node
        #         for childNode in node.children:
        #             childDict.add(childNode.val)
        #             if childNode.val in parentDict:
        #                 del parentDict[childNode.val]
        
        # for item in parentDict.values():
        #     return item