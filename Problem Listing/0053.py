# https://leetcode.com/problems/maximum-subarray/
# 47 ms, 31.31 MB

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res, sum = nums[0], 0
        for n in nums:
            if sum < 0:
                sum = 0
            sum += n
            res = max(res, sum)
        return res
