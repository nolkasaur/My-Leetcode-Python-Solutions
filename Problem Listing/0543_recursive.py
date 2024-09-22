# https://leetcode.com/problems/diameter-of-binary-tree/
# 39 ms, 19.34 MB

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.res = 0

        def rec_func(curr):
            if not curr:
                return 0
            leftChild = rec_func(curr.left)
            rightChild = rec_func(curr.right)
            self.res = max(self.res, leftChild + rightChild)
            return 1 + max(leftChild, rightChild)

        rec_func(root)
        return self.res
