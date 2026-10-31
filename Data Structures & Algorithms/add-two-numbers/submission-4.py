# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        curr = dummy
        carry = 0
        while l1 or l2:
            res = carry
            if l1:
                res += l1.val
            if l2:
                res += l2.val
            if res >= 10:
                carry = 1
                res = res % 10
            else:
                carry = 0
            curr.next = ListNode(res)
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
            curr = curr.next
        if carry:
            curr.next = ListNode(1)
        return dummy.next