# https://leetcode.com/problems/longest-consecutive-sequence/
# 357 ms, 34.94 MB

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = list(dict.fromkeys(nums))
        nums.sort()
        aux, res = 0, 0
        if len(nums) == 0: return 0
        if len(nums) == 1: return 1
        for i in range(len(nums)-1):
            if nums[i+1]-1 != nums[i]:
                if aux > res: res = aux
                aux = 0
            else:
                aux+=1
        if aux > res: res = aux
        res+=1
        return res
