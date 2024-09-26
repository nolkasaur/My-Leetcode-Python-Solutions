# https://leetcode.com/problems/single-number/
# 107 ms, 19.18 MB

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        return reduce (lambda a,b: a^b, nums)
