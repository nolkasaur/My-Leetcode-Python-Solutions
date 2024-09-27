# https://leetcode.com/problems/counting-bits/
# 66 ms, 23.31 MB

class Solution:
    def countBits(self, n: int) -> List[int]:
        res, significant_bit = [0]*(n+1), 1
        for i in range(1, n+1):
            if i == significant_bit * 2:
                significant_bit *= 2
            res[i] = res[i-significant_bit] + 1
        return res
