# https://leetcode.com/problems/number-of-1-bits/
# 31 ms, 16.57 MB

class Solution:
    def hammingWeight(self, n: int) -> int:
        res = 0
        bin = format(n, 'b')
        for i in bin:
            if i == '1':
                res += 1
        return res
