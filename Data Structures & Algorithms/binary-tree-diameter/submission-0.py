# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        if not root.left and not root.right:
            return 0
        
        def max_height(root):
            if not root:
                return 0
            return 1 + max(max_height(root.left), max_height(root.right))

        left_height = max_height(root.left)
        right_height = max_height(root.right)
        curr_length = left_height + right_height
        left_max_length = self.diameterOfBinaryTree(root.left)
        right_max_length = self.diameterOfBinaryTree(root.right)
        return max(curr_length, left_max_length, right_max_length)
        