# https://leetcode.com/problems/climbing-stairs/
# 40 ms, 16.32 MB

class Solution:
    def climbStairs(self, n: int) -> int:
        one_step, two_steps = 1, 1
        for i in range(n-1):
            aux = one_step
            one_step += two_steps
            two_steps = aux
        return one_step
