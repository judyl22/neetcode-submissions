# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head:
            return
        if not head.next:
            return
        slow, fast = head, head.next # so slow will not go onto len / 2 + 1 if even length
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        list2 = slow.next
        slow.next = None
        list1 = head # list1 will always longer than list2

        # reverse list2
        prev, curr = None, list2
        while curr:
            temp_next = curr.next
            curr.next = prev
            prev, curr = curr, temp_next
        list2 = prev

        while list2:
            temp1 = list1.next
            temp2 = list2.next
            list1.next = list2
            list2.next = temp1
            list1, list2 = temp1, temp2
