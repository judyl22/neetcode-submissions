# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # brute force: O(n^2)
        if not root:
            return True
        def dfs(root, small, large):
            if not root:
                return True
            if root.val <= small or root.val >= large:
                return False
            return dfs(root.left, small, root.val) and dfs(root.right, root.val, large)
        
        return dfs(root, float('-inf'), float('inf'))