import math
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def sortedArrayToBST(nums):
    # recursion user solution 2
        def recursiveNodeBuild(low,high):
            if low > high:
                return None
            
            mid = (low+high)//2
            return TreeNode(nums[mid],recursiveNodeBuild(low,mid-1),recursiveNodeBuild(mid+1,high))
        
        return recursiveNodeBuild(0,len(nums)-1)

        # recursion user solution
        # total_nums = len(nums)
        # if not total_nums:
        #     return None

        # mid_node = total_nums // 2
        # return TreeNode(
        #     nums[mid_node], 
        #     self.sortedArrayToBST(nums[:mid_node]), self.sortedArrayToBST(nums[mid_node + 1 :])
        # )
        
    # Iterative approach(didnt complete, did not find any solution with iterative)
    # contStack = []
    # breakStack = []
    # j = 0
    # for i in range(0,len(nums)):
    #     contStack.append(TreeNode(nums[i]))
    #     if i == 1 or i == j+3:
    #         j = i
    #         breakStack.append(TreeNode(nums[i]))
        
    #     if len(contStack) == 3:
    #         right = contStack.pop()
    #         root = contStack.pop()
    #         left = contStack.pop()
    #         root.left = left
    #         root.right = right
        
    #     if len(breakStack) == 3:
    #         right = contStack.pop()
    #         root = contStack.pop()
    #         left = contStack.pop()
    #         root.left = left
    #         root.right = right

    # Recursive, My Approach
    # if len(nums)==1:
    #     return TreeNode(nums[0])
    # elif len(nums) == 0:
    #     return
    # nodeLeft = sortedArrayToBST(nums[0:math.floor(len(nums)/2)])
    # nodeRight = sortedArrayToBST(nums[math.floor(len(nums)/2)+1:])
    # nodeRoot = TreeNode(nums[math.floor(len(nums)/2)])
    # nodeRoot.left = nodeLeft
    # nodeRoot.right = nodeRight
    # return nodeRoot

# Used inorder traversal from a different leet code problem solution to print and test
# if building BST is successful
def inorderTraversal(root):
# Recursive solution
    result = []
    def recursiveInOrder(root):
        if root == None:
            return
        else:
            recursiveInOrder(root.left)
            result.append(root.val)
            recursiveInOrder(root.right)
            return

    recursiveInOrder(root)   
    return result 

if __name__ == "__main__":
    nums = [-10,-3,0,5,9,11,15,16,20,25]
    print(inorderTraversal(sortedArrayToBST(nums)))