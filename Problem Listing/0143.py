# https://leetcode.com/problems/reorder-list/
# 56 ms, 24.73 MB

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        # "split" the list in two halves, by finding the middle point
        slow_iterator, fast_iterator = head, head.next
        while fast_iterator and fast_iterator.next:
            slow_iterator = slow_iterator.next
            fast_iterator = fast_iterator.next.next

        # reverse the second half of the list
        second_list = slow_iterator.next
        prev = slow_iterator.next = None
        while second_list:
            tmp = second_list.next
            second_list.next = prev
            prev = second_list
            second_list = tmp

        # merge, alternately, the first and second halves
        first, second = head, prev
        while second:
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first = tmp1
            second = tmp2
