import queue
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class BinaryTree:
    def __init__(self,nodes=None):
          nodeQueue = queue.Queue()
          if nodes is None:
            self.root = None
          else:
            node = TreeNode(nodes[1])
            self.root = node
            for i in range(2,len(nodes)):
                if i%2 == 0:
                    left =  TreeNode(nodes[i])
                    node.left = left
                    nodeQueue.put(left)
                else:
                    right = TreeNode(nodes[i])
                    node.right = right
                    nodeQueue.put(right)
                    node = nodeQueue.get()

# def inorderTraversal(root):
# # Recursive solution
#     result = []
#     def recursiveInOrder(root):
#         if root == None:
#             return
#         else:
#             recursiveInOrder(root.left)
#             result.append(root.val)
#             recursiveInOrder(root.right)
#             return

#     recursiveInOrder(root)   
#     return result 

def maxDepth(root):
        # recursive
        # if root != None:
        #     return 1 + max(maxDepth(root.left),maxDepth(root.right))
        # else:
        #     return 0

        # Iterative
        # if root == None:
        #     return 0
        # nodeQueue = queue.Queue()
        # nodeQueue.put(root)
        # level = 0
        # while not nodeQueue.empty():
        #     level += 1
        #     for i in range(0,nodeQueue.qsize()):
        #         # print(nodeQueue.qsize())
        #         node = nodeQueue.get()
        #         if node.left != None:
        #             nodeQueue.put(node.left)
        #         if node.right != None:
        #             nodeQueue.put(node.right)
        
        # return level

        # Iterative 2
        nodeDepthList = []
        nodeDepthList.append([root,1])
        res = 1

        while bool(nodeDepthList):
            node,depth = nodeDepthList.pop()
            if node:
                res = max(res,depth)
                nodeDepthList.append([node.right,depth+1])
                nodeDepthList.append([node.left,depth+1])
        
        return res

            



        # nodeList = []
        # depthList = []
        # node = root
        # depth = 1

        # while node != None or bool(nodeList):
        #     while node != None:
        #         nodeList.append(node)
        #         depth += 1
        #         node = node.left
            
        #     node = nodeList.pop()
        #     node = node.right
        #     depth -= 1
        #     if node == None:
        #         depthList.append(depth)

if __name__ == "__main__":
     nodes = [0,3,1,2,4,9,10,None,None,None,None,None,None,5,None,None,None,None,None,None,None,None,None,None,None,None,None,6,None,None,None,None]
     binaryTree = BinaryTree(nodes)
     print(maxDepth(binaryTree.root))
    #  print(inorderTraversal(binaryTree.root))