# https://leetcode.com/problems/linked-list-cycle/
# 49 ms, 19.49 MB

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        found_hashset = set()
        while head:
            if head in found_hashset:
                return True
            else:
                found_hashset.add(head)
            head = head.next
        return False
