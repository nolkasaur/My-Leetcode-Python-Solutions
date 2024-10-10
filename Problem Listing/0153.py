# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/
# 51 ms, 16.99 MB

class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, mid, right, res = 0, 0, len(nums)-1, 5000
        while left <= right:
            mid = (left+right) //2
            if nums[mid] < nums[left]:
                res = min(res, nums[mid])
                right = mid - 1
            else:
                res = min(res, nums[left])
                left = mid + 1
        return res
