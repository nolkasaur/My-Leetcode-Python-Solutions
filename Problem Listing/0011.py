# https://leetcode.com/problems/container-with-most-water/
# 506 ms, 29.30 MB

class Solution:
    def maxArea(self, height: List[int]) -> int:
        left_bound, right_bound, res = 0, len(height)-1, 0
        while left_bound < right_bound:
            area = (right_bound - left_bound) * min(height[left_bound], height[right_bound])
            if area > res: res = area
            if height[left_bound] < height[right_bound]:
                left_bound += 1
            else:
                right_bound -= 1
        return res
