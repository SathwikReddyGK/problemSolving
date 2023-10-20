class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class LinkedList:
    def __init__(self,nodes=None):
          if nodes is None:
            self.head = None
          else:
            node = ListNode(nodes.pop(0))
            self.head = node
            for elem in nodes:
                 node.next = ListNode(elem)
                 node = node.next
                 
def reverseList(head):
    # itertative solution
    prev = None
    while head.next != None:
        next = head.next
        head.next = prev
        prev = head
        head = next
    
    head.next = prev
    return head

        
    # recursive solution
        # def recursive(node, prevNode):
        #      if node.next is None:
        #           node.next = prevNode
        #           return node
        #      else:
        #           node2 = recursive(node.next,node)
        #           node.next = prevNode
        #           return node2
        
        # return recursive(head,None)

if __name__ == "__main__":
     nodes = [1,2,3,4,5]
     linkedList = LinkedList(nodes)
     head = reverseList(linkedList.head)
     print(head.val)