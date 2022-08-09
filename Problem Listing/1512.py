# https://leetcode.com/problems/number-of-good-pairs/
# 68 ms, 13.9 MB

class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        res = 0
        for x in range(0,len(nums)-1):
            for y in range(x+1,len(nums)):
                if nums[x] == nums[y]:
                    res+=1
        return res
