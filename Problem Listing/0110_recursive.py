# https://leetcode.com/problems/balanced-binary-tree/
# 48 ms, 17.77 MB

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        def rec_func(curr):
            if not curr:
                return [True, 0]
            leftChild = rec_func(curr.left)
            rightChild = rec_func(curr.right)
            balanced = leftChild[0] and rightChild[0] and abs(leftChild[1]-rightChild[1])<=1
            return [balanced, 1 + max(leftChild[1], rightChild[1])]

        return rec_func(root)[0]
