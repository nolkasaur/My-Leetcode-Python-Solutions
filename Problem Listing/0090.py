# https://leetcode.com/problems/subsets-ii/
# 0 ms, 16.70 MB

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        def backtrack(index, sub_set):
            if index == len(nums):
                res.append(sub_set[::])
                return
            sub_set.append(nums[index])
            backtrack(index + 1, sub_set)
            sub_set.pop()
            while index + 1 < len(nums) and nums[index] == nums[index + 1]:
                index += 1
            backtrack(index + 1, sub_set)
        backtrack(0, [])
        return res

            
