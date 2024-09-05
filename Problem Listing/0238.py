# https://leetcode.com/problems/product-of-array-except-self/
# 264 ms, 25.7 MB

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res, pre, post = [1]*len(nums), 1, 1
        for i in range(0, len(nums)):
            res[i] = pre
            pre *= nums[i]
        for j in range(len(nums)-1, -1, -1):
            res[j] *= post
            post *= nums[j]
        return res
