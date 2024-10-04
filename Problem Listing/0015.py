# https://leetcode.com/problems/3sum/
# 1738 ms, 20.71 MB

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        i = 0
        while i < len(nums)-2:
            target = -nums[i]
            left_bound, right_bound = i+1, len(nums)-1
            while left_bound < right_bound:
                sum = nums[left_bound] + nums[right_bound]
                if i > 0 and nums[i] == nums[i-1]:
                    left_bound += 1
                    continue
                elif sum == target:
                    res.append([nums[i], nums[left_bound], nums[right_bound]])
                    left_bound += 1
                    while nums[left_bound] == nums[left_bound-1] and left_bound < right_bound:
                        left_bound += 1
                elif sum > target:
                    right_bound -= 1
                else:
                    left_bound += 1
            i += 1
        return res
