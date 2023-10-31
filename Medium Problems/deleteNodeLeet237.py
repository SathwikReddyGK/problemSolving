class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def deleteNode(node):
    # User Solution, improvised version of mine, we dont need to iterate over the list
    # just changing existing node and point to the proper next should be fine
    node.val = node.next.val
    node.next = node.next.next
    # My Solution
    # interNode = node.next
    # node.val = interNode.val
    # node.next = interNode.next

    # while interNode.next != None:
    #     interNode2 = interNode
    #     interNode.val = interNode2.val
    #     interNode.next = interNode2.next
    #     interNode = interNode2.next

def buildList(nums,returnVal):
    node = ListNode(None)
    returnNode = node
    head = node
    
    for i in range(len(nums)):
        node.val = nums[i]
        if node.val == returnVal:
            returnNode = node
        if i != len(nums) - 1:
            node.next = ListNode(None)
            node = node.next

    return returnNode,head

def printList(head):
    out = []
    while head != None:
        out.append(head.val)
        head = head.next
    
    print(out)

if __name__ == "__main__":
    nums = [4,5,1,9]
    nodeToBeDeleted,head = buildList(nums,5)
    deleteNode(nodeToBeDeleted)
    printList(head)
