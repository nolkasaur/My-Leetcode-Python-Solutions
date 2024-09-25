# https://leetcode.com/problems/subtree-of-another-tree/
# 74 ms, 16.92 MB

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        def sameTree(root, subRoot):
            if not root and not subRoot:
                return True
            elif not root or not subRoot:
                return False
            elif root.val == subRoot.val:
                return sameTree(root.left, subRoot.left) and sameTree(root.right, subRoot.right)
            else:
                return False

        if not root and not subRoot:
            return True
        elif not root or not subRoot:
            return False
        elif root.val == subRoot.val:
            return (sameTree(root.left, subRoot.left) and sameTree(root.right, subRoot.right)) or self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
        else:
            return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
