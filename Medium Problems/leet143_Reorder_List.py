# You are given the head of a singly linked-list. The list can be represented as:

# L0 → L1 → … → Ln - 1 → Ln
# Reorder the list to be on the following form:

# L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …
# You may not modify the values in the list's nodes. Only nodes themselves may be changed.

 

# Example 1:


# Input: head = [1,2,3,4]
# Output: [1,4,2,3]
# Example 2:


# Input: head = [1,2,3,4,5]
# Output: [1,5,2,4,3]
 

# Constraints:

# The number of nodes in the list is in the range [1, 5 * 104].
# 1 <= Node.val <= 1000
# Definition for singly-linked list.
from collections import deque
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reorderList(head):
    """
    Do not return anything, modify head in-place instead.
    """
    # User solution1, 
    if head.next == None or head.next.next == None:
        return
    oneP = head
    twoP = head
    while twoP.next and twoP.next.next:
        oneP = oneP.next
        twoP = twoP.next.next
    
    temp = oneP
    prev,oneP = None,oneP.next
    while oneP:
        next = oneP.next
        oneP.next = prev
        prev = oneP
        oneP = next
    
    temp.next = None

    head1 = head
    while prev:
        next = head1.next
        head1.next = prev
        head1 = head1.next
        prev = next


    # prev,oneP = oneP.next,oneP.next.next
    # prev.next = None
    # while oneP:
    #     next = oneP.next
    #     oneP.next = prev
    #     prev = oneP
    #     oneP = next
    
    # head1 = head

    # while head1 and prev:
    #     next = head1.next
    #     head1.next = prev
    #     prev = next
    #     head1 = head1.next
    
    # head1.next.next = None



    # My approach of using a stack was implemented by a user, implementing that
    # stack = deque()
    # headVar = head
    # while headVar:
    #     stack.append(headVar)
    #     headVar = headVar.next
    
    # headVar = head
    # n = 0
    # while headVar:
    #     next = headVar.next
    #     curr = stack.pop()
    #     headVar.next = curr

    # Tried a method, which was created too many edge cases and was not working
    # reverseHead = ListNode(head.val,None)
    # temp2 = ListNode(head.next.val,head.next.next)

    # while temp2 != None:
    #     temp = ListNode(temp2.val,reverseHead)
    #     reverseHead = temp
    #     temp2 = temp2.next
    
    # temp3 = head
    # while temp3 and reverseHead:
    #     next = temp3.next
    #     temp3.next = reverseHead
    #     reverseHead = next
    #     temp3 = temp3.next


if __name__ == "__main__":
    headList = [1,2,3,4,5]

    head = ListNode(headList[0])
    curr = head

    for i in range(1,len(headList)):
        curr.next = ListNode(headList[i])
        curr = curr.next
    
    reorderList(head)
    # print(head)
    while head:
        print(head.val)
        head = head.next


        