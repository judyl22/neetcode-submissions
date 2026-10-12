# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root and not subRoot:
            return True
        elif not root or not subRoot:
            return False
        
        def dfs(root, val):
            if not root:
                return False
            elif root.val == val:
                if sameTree(root, subRoot):
                    return True
            return dfs(root.left, val) or dfs(root.right, val)

        def sameTree(root, subRoot):
            if not root and not subRoot:
                return True
            elif not root or not subRoot or root.val != subRoot.val:
                return False
            return sameTree(root.left, subRoot.left) and sameTree(root.right, subRoot.right)
        
        return dfs(root, subRoot.val)
        