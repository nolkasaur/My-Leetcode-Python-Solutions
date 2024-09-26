# https://leetcode.com/problems/number-of-1-bits/
# 36 ms, 16.43 MB

class Solution:
    def hammingWeight(self, n: int) -> int:
        res = 0
        while n:
            n = n & (n-1)
            res += 1
        return res
