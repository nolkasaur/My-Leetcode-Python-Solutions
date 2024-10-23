# https://leetcode.com/problems/kth-largest-element-in-an-array/
# 83 ms, 27.55 MB

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums = [-n for n in nums]
        heapq.heapify(nums)
        res = None
        for i in range(k):
            res = heapq.heappop(nums)
        return -res
