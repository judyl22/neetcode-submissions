# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        is_balance = True

        def dfs(root):
            nonlocal is_balance

            if not root:
                return 0
            left_height = dfs(root.left)
            right_height = dfs(root.right)
            curr_balance = (abs(left_height - right_height) <= 1)
            is_balance = is_balance and curr_balance
            return 1 + max(left_height, right_height)
        
        dfs(root)
        return is_balance