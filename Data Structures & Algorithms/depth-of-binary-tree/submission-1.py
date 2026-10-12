# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        queue = deque()
        queue.append((root, 1))
        max_depth = 0
        while queue:
            for i in range(len(queue)):
                [curr, depth] = queue.popleft()
                if curr:
                    max_depth = max(max_depth, depth)
                    queue.append((curr.left, depth + 1))
                    queue.append((curr.right, depth + 1))
        return max_depth