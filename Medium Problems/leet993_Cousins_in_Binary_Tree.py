# Description
# Given the root of a binary tree with unique values and the values of two different nodes of the tree x and y, return true if the nodes corresponding to the values x and y in the tree are cousins, or false otherwise.

# Two nodes of a binary tree are cousins if they have the same depth with different parents.

# Note that in a binary tree, the root node is at the depth 0, and children of each depth k node are at the depth k + 1.

 

# Example 1:


# Input: root = [1,2,3,4], x = 4, y = 3
# Output: false
# Example 2:


# Input: root = [1,2,3,null,4,null,5], x = 5, y = 4
# Output: true
# Example 3:


# Input: root = [1,2,3,null,4], x = 2, y = 3
# Output: false
 

# Constraints:

# The number of nodes in the tree is in the range [2, 100].
# 1 <= Node.val <= 100
# Each node has a unique value.
# x != y
# x and y are exist in the tree.

# Solution

# // Time Complexity : BFS - O(N) since we are traversing all the nodes
#                      DFS - O(N) since we are traversing all the nodes
# // Space Complexity : BFS(both with and without parent queue) - O(N) it is actually O(N/2) since in worst case, 
#                       the balanced binary tree will have n/2 leaf nodes and we are using a stack to keep the nodes and 
#                       respective parents of each level to be processed next. 
#                       DFS - O(N) since implicit stack in DFS will need space and in worst case we can have skewed binary tree
#                       where all the nodes are skewed to right or left
# // Did this code successfully run on Leetcode : Yes
# // Any problem you faced while coding this : None


# // Your code here along with comments explaining your approach
# Approach is to use BFS or DFS to traverse the entire binary tree and keep checking if a node value is matching with the given
# values and if it matches then check if both parents are different, if different then true else False
# In BFS we can do it in both ways, with or without parent queue. When going with parent queue, as we append the next level
# nodes to be processed we will also append respective parents so that at same index of two different queue, we find node and
# it's parent. By this we can compare the parents of x and y along with value
# In DFS we can use global variables to maintain if x and y is found and their parents. Once traversal is completed we can check
# to see if the values are cousins


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

xLevel = 0
yLevel = 0
xParent = None
yParent = None

def isCousins(root, x, y):
        # DFS
        global xLevel
        global yLevel
        global xParent
        global yParent

        def helper(node,level,parent):
            global xLevel
            global yLevel
            global xParent
            global yParent
            
            if node.val == x:
                xLevel = level
                xParent = parent
                return
            
            if node.val == y:
                yLevel = level
                yParent = parent
                return
            
            if node.left != None:
                helper(node.left,level+1,node)
            
            if node.right != None:
                helper(node.right,level+1,node)
        
        xLevel = 0
        yLevel = 0
        xParent = None
        yParent = None

        if root != None:
            helper(root,0,None)

        if xLevel == yLevel and xParent != yParent:
            return True
        
        return False
        # BFS Avoiding parent queue
        # nodeQueue = deque()
        # if root.val == x or root.val == y:
        #     return False

        # nodeQueue.append(root)
        # prevCount = 1
        
        # xFound = False
        # yFound = False

        # while nodeQueue:
        #     curCount = 0
        #     while prevCount > 0:
        #         node = nodeQueue.popleft()
                
        #         prevCount -= 1
                                
        #         if node.left != None:
        #             if node.left.val == x:
        #                 xFound = True
        #             elif node.left.val == y:
        #                 yFound = True
        #             nodeQueue.append(node.left)
        #             curCount += 1
                
        #         if node.right != None:
        #             if node.right.val == x:
        #                 xFound = True
        #             elif node.right.val == y:
        #                 yFound = True
        #             nodeQueue.append(node.right)
        #             curCount += 1
                
        #         if (node.left != None and (node.left.val == x or node.left.val == y)) and (node.right != None and (node.right.val == x or node.right.val == y)):
        #             return False
                
        #     prevCount = curCount
        #     if xFound == True and yFound == True:
        #         return True
        #     elif xFound == True or yFound == True:
        #         return False
        
        # return False

        # BFS using parent queue
        # Using parent queue
        # nodeQueue = deque()
        # parentQueue = deque()

        # nodeQueue.append(root)
        # prevCount = 1
        # parentQueue.append(None)

        # xFound = False
        # yFound = False
        # xParent = None
        # yParent = None

        # while nodeQueue:
        #     curCount = 0
        #     while prevCount > 0:
        #         node = nodeQueue.popleft()
        #         parent = parentQueue.popleft()
        #         prevCount -= 1
        #         if node.val == x:
        #             xFound = True
        #             xParent = parent
                
        #         if node.val == y:
        #             yFound = True
        #             yParent = parent
                
        #         if node.left != None:
        #             nodeQueue.append(node.left)
        #             parentQueue.append(node)
        #             curCount += 1
                
        #         if node.right != None:
        #             nodeQueue.append(node.right)
        #             parentQueue.append(node)    
        #             curCount += 1
                
        #     prevCount = curCount
        #     if xFound == True and yFound == True:
        #         if xParent == yParent:
        #             return False
        #         else:
        #             return True
        #     elif xFound == True or yFound == True:
        #         return False
        
        # return False

if __name__ == "__main__":
    ar = [1,2,3,4]
    n = len(ar)
    root = TreeNode(ar[0],buildLinkedList(1,n),buildLinkedList(2,n))
    x = 4
    y  = 3

    print(isCousins(root, x, y))