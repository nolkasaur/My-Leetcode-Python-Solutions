# https://leetcode.com/problems/copy-list-with-random-pointer/
# 38 ms, 17.54

"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        hashmap = {None:None}
        curr = head
        while curr:
            copy = Node(curr.val)
            hashmap[curr] = copy
            curr = curr.next
        curr = head
        while curr:
            copy = hashmap[curr]
            copy.next = hashmap[curr.next]
            copy.random = hashmap[curr.random]
            curr = curr.next
        return hashmap[head]
