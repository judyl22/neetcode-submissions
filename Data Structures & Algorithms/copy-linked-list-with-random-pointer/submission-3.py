"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        copy_map = {None: None}
        dummy = Node(0)
        curr = dummy
        while head:
            if head not in copy_map:
                copy_map[head] = Node(head.val)
            curr.next = copy_map[head]
            if head.random not in copy_map:
                copy_map[head.random] = Node(head.random.val)
            curr.next.random = copy_map[head.random]
            head = head.next
            curr = curr.next
        return dummy.next