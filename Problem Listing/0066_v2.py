# https://leetcode.com/problems/plus-one/
# 41 ms, 16.51

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        return [int(x) for x in list(str(int("".join([str(x) for x in digits])) + 1))]
