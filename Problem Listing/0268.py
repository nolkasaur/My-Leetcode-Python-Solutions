# https://leetcode.com/problems/missing-number/
# 117 ms, 17.79 MB

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        xor_nums, xor_full = 0, 0
        for i in range(len(nums)+1):
            xor_full ^= i
        for i in range(len(nums)):
            xor_nums ^= nums[i]
        return xor_full ^ xor_nums
