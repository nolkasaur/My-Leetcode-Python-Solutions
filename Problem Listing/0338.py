# https://leetcode.com/problems/counting-bits/
# 114 ms, 23.37 MB

class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = []
        for i in range(n+1):
            ans.append(self.getNrOnes(i))
        return ans

    def getNrOnes(self, n):
        res = 0
        while n:
            res += n % 2
            n >>= 1
        return res
