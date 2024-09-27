# https://leetcode.com/problems/missing-number/
# 116 ms, 17.98 MB

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        full_list = [x for x in range(len(nums)+1)]
        return sum(full_list) - sum(nums)
