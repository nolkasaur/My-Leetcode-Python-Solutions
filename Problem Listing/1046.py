# https://leetcode.com/problems/last-stone-weight/
# 33 ms, 16.63 MB

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-s for s in stones]
        heapq.heapify(stones)
        while len(stones) > 1:
            first = heapq.heappop(stones)
            second = heapq.heappop(stones)
            if first != second:
               heapq.heappush(stones, first - second)
        if stones:
            return abs(stones[0])
        return 0
