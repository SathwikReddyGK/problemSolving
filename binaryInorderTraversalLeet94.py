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

def inorderTraversal(root):
# Solution suggested by a user is translated to python
        result = []
        nodeList = []
        currentNode = root

        while currentNode != None or bool(nodeList):
            while currentNode != None:
                nodeList.append(currentNode)
                currentNode = currentNode.left
            
            currentNode = nodeList.pop()
            result.append(currentNode.val)
            currentNode = currentNode.right
        
        return result

if __name__ == "__main__":
     nodes = [0,3,1,2,4,9,10,None,5,6]
     binaryTree = BinaryTree(nodes)
     print(inorderTraversal(binaryTree.root))
     
     