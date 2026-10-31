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
        copy_map = {}
        new_head = Node(0)
        curr = new_head
        while head:
            if head in copy_map:
                curr.next = copy_map[head]
            else:
                curr.next = Node(head.val)
                copy_map[head] = curr.next
            if head.random == None:
                curr.next.random = None
            elif head.random in copy_map:
                curr.next.random = copy_map[head.random]
            else:
                curr.next.random = Node(head.random.val)
                copy_map[head.random] = curr.next.random
            head = head.next
            curr = curr.next
        return new_head.next