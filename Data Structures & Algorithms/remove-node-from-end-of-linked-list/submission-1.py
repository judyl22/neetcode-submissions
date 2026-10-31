# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        pointer2 = head
        apart = 0
        while apart < n:
            apart += 1
            pointer2 = pointer2.next
        if not pointer2: # remove the first node
            return head.next
        pointer2 = pointer2.next # want pointer1 stop before the node to remove
        pointer1 = head
        while pointer2:
            pointer1 = pointer1.next
            pointer2 = pointer2.next
        pointer1.next = pointer1.next.next
        return head
        