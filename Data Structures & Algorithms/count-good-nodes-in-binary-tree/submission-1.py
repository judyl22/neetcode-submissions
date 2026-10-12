# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        stack = []
        res = 0
        if not root:
            return 0
        stack.append((root, float('-inf')))
        while stack:
            node, large_val = stack.pop()
            if node.val >= large_val:
                res += 1
            if node.left:
                stack.append((node.left, max(node.val, large_val)))
            if node.right:
                stack.append((node.right, max(node.val, large_val)))
        return res