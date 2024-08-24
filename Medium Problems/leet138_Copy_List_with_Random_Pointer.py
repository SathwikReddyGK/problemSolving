# Problem
# 138. Copy List with Random Pointer

# A linked list of length n is given such that each node contains an additional random pointer, which could point to any node in the list, or null.

# Construct a deep copy of the list. The deep copy should consist of exactly n brand new nodes, where each new node has its value set to the value of its corresponding original node. Both the next and random pointer of the new nodes should point to new nodes in the copied list such that the pointers in the original list and copied list represent the same list state. None of the pointers in the new list should point to nodes in the original list.

# For example, if there are two nodes X and Y in the original list, where X.random --> Y, then for the corresponding two nodes x and y in the copied list, x.random --> y.

# Return the head of the copied linked list.

# The linked list is represented in the input/output as a list of n nodes. Each node is represented as a pair of [val, random_index] where:

# val: an integer representing Node.val
# random_index: the index of the node (range from 0 to n-1) that the random pointer points to, or null if it does not point to any node.
# Your code will only be given the head of the original linked list.

# Example 1:


# Input: head = [[7,null],[13,0],[11,4],[10,2],[1,0]]
# Output: [[7,null],[13,0],[11,4],[10,2],[1,0]]
# Example 2:


# Input: head = [[1,1],[2,1]]
# Output: [[1,1],[2,1]]
# Example 3:



# Input: head = [[3,null],[3,0],[3,null]]
# Output: [[3,null],[3,0],[3,null]]
 

# Constraints:

# 0 <= n <= 1000
# -104 <= Node.val <= 104
# Node.random is null or is pointing to some node in the linked list.

# Solution

# // Time Complexity : O(N)
# // Space Complexity : O(N) - Dictionary
# // Did this code successfully run on Leetcode : Yes
# // Any problem you faced while coding this : No

# // Your code here along with comments explaining your approach
# Approach is to go over the linked list and create nodes and random nodes and keep adding them into dictionary
# anytime we are trying to create a node, we can check in dictionary if it is already created.

# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


def buildNextAndRandom(nodeDict,retNode,curNode):
    if curNode.next != None:
        if curNode.next not in nodeDict:
            retNode.next = Node(curNode.next.val)
            nodeDict[curNode.next] = retNode.next
        else:
            retNode.next = nodeDict[curNode.next]
    else:
        retNode.next = None
    
    if curNode.random != None:
        if curNode.random not in nodeDict:
            retNode.random = Node(curNode.random.val)
            nodeDict[curNode.random] = retNode.random
        else:
            retNode.random = nodeDict[curNode.random]
    else:
        retNode.random = None

def copyRandomList(head):
    nodeDict = {}
    
    if head == None:
        return head
    
    curr = head
    retHead = Node(curr.val)
    nodeDict[curr] = retHead

    buildNextAndRandom(nodeDict,retHead,curr)

    curr = head.next
    
    while curr != None:
        newNode = nodeDict[curr]
        
        buildNextAndRandom(nodeDict,newNode,curr)

        curr = curr.next

    return retHead

if __name__ == "__main__":
    # This doesnt run since linked list is not created
    # head = [[1,1],[2,1]]
    # head = [[3,null],[3,0],[3,null]]
    head = [[7,None],[13,0],[11,4],[10,2],[1,0]]
    copyRandomList(head)