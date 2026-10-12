# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        inorder_dict = {}
        for i, num in enumerate(inorder):
            inorder_dict[num] = i
        
        def dfs(pre_left, pre_right, in_left, in_right):
            if pre_left > pre_right or in_left > in_right:
                return None
            root = TreeNode(preorder[pre_left])
            inorder_index = inorder_dict[preorder[pre_left]]
            left_length = inorder_index - in_left
            root.left = dfs(pre_left + 1, pre_left + left_length, in_left, inorder_index - 1)
            root.right = dfs(pre_left + left_length + 1, pre_right, inorder_index + 1, in_right)
            return root
        
        return dfs(0, len(preorder) - 1, 0, len(preorder) - 1)
