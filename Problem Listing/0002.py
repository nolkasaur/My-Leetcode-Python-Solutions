# https://leetcode.com/problems/add-two-numbers/
# 48 ms, 16.71 MB

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        curr = dummy
        carry = 0
        while l1 or l2 or carry:
            d1 = l1.val if l1 else 0
            d2 = l2.val if l2 else 0
            sum = d1 + d2 + carry
            carry = sum // 10 # get the tens place, aka our carry
            sum = sum % 10 # get the ones place only
            curr.next = ListNode(sum)
            curr = curr.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        return dummy.next
