# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        ans = []
        queue = deque()
        queue.append(root)
        while queue:
            last_node = None
            for i in range(len(queue)):
                node = queue.popleft()
                if node:
                    last_node = node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            ans.append(last_node)
        return ans