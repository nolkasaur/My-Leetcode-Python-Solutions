# https://leetcode.com/problems/koko-eating-bananas/
# 264 ms, 18.08 MB

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, mid, right, res = 1, 0, max(piles), max(piles)
        while left <= right:
            mid = (left + right) // 2
            hours_count = 0
            for p in piles:
                hours_count += math.ceil(p/mid)
            if hours_count > h:
                left = mid + 1
            else:
                res = min(res, mid)
                right = mid - 1
        return res
