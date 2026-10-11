# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return root
        curr = root
        temp = curr.right
        curr.right = curr.left
        curr.left = temp
        self.invertTree(curr.left)
        self.invertTree(curr.right)
        return root
        