# https://leetcode.com/problems/reverse-bits/
# 33 ms, 16.47 MB

class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        for i in range(32):
            bit = (n >> i) & 1 # get the (last - i) bit of n
            res = res | bit << (31 - i) # put that bit at the (start + 1) position of res
        return res
