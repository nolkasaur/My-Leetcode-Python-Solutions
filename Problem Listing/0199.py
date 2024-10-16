# https://leetcode.com/problems/binary-tree-right-side-view/
# 39 ms, 16.58 MB

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        queue = collections.deque([root])
        while queue:
            rightest_node = None
            queue_len = len(queue)
            for i in range(queue_len):
                node = queue.popleft()
                if node:
                    rightest_node = node
                    queue.append(node.left)
                    queue.append(node.right)
            if rightest_node:
                res.append(rightest_node.val)
        return res
