# https://leetcode.com/problems/search-in-rotated-sorted-array/
# 52 ms, 17.00 MB

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, mid, right, res = 0, 0, len(nums)-1, -1
        while left <= right:
            mid = (left+right) //2
            if target == nums[mid]:
                return mid
            if nums[left] <= nums[mid]:
                if target > nums[mid] or target < nums[left]:
                    left = mid + 1
                else:
                    right = mid - 1
            else:
                if target > nums[mid] and target < nums[left]:
                    left = mid + 1
                else:
                    right = mid - 1
        return res
