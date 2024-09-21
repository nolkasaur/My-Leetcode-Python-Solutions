# https://leetcode.com/problems/reverse-linked-list/
# 35 ms, 17.78 MB

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr, prev = head, None
        while curr:
            next_aux = curr.next
            curr.next = prev
            prev = curr
            curr = next_aux
        return prev
