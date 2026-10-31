# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        dummy = ListNode(0)
        curr = dummy
        while l1 and l2:
            value = l1.val + l2.val + carry
            if value > 9:
                carry = 1
                value = value % 10
            else:
                carry = 0
            curr.next = ListNode(value)
            curr = curr.next
            l1 = l1.next
            l2 = l2.next
        if l1:
            remain = l1
        elif l2:
            remain = l2
        else:
            if carry:
                curr.next = ListNode(1)
            return dummy.next
        while remain:
            value = remain.val + carry
            if value > 9:
                carry = 1
                value = value % 10
            else:
                carry = 0
            curr.next = ListNode(value)
            remain = remain.next
            curr = curr.next
        if carry:
            curr.next = ListNode(1)
        return dummy.next
        