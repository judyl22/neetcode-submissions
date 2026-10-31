# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length = 0
        curr = head
        while curr:
            length += 1
            curr = curr.next
        need = length - n + 1
        if need == 1:
            return head.next
        prev = head
        while need != 2:
            prev = prev.next
            need -= 1
        prev.next = prev.next.next
        return head
        

        