# https://leetcode.com/problems/binary-search/
# 197 ms, 18.09 MB

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low, mid, high = 0, 0, len(nums)-1
        while low <= high:
            mid = (low + high) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
        return -1
