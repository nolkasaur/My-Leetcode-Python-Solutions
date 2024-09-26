# https://leetcode.com/problems/number-of-1-bits/
# 33 ms, 16.6 MB

class Solution:
    def hammingWeight(self, n: int) -> int:
        res = 0
        while n:
            res += n % 2
            n >>= 1
        return res
