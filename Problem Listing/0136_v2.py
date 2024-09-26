# https://leetcode.com/problems/single-number/
# 110 ms, 19.03 MB

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = 0
        for n in nums:
            res ^= n
        return res
