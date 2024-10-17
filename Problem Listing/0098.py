# https://leetcode.com/problems/validate-binary-search-tree/
# 0 ms, 18.81 MB

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def dfs(node, min, max):
            if node:
                if node.val > min and node.val < max and dfs(node.left, min, node.val) and dfs(node.right, node.val, max):
                    return True
                else:
                    return False
            return True

        return dfs(root, float("-inf"), float("inf"))
