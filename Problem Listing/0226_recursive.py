# https://leetcode.com/problems/invert-binary-tree/
# 25 ms, 16.56 MB

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        left_aux = root.left
        root.left = root.right
        root.right = left_aux
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root
