# https://leetcode.com/problems/daily-temperatures/
# 903 ms, 32.44 MB

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res, stack = [0] * len(temperatures), []
        for index, temp in enumerate(temperatures):
            while stack and temp > stack[-1][0]:
                stack_temp, stack_index = stack.pop()
                res[stack_index] = index - stack_index
            stack.append([temp, index])
        return res
