# https://leetcode.com/problems/generate-parentheses/
# 47 ms, 17.02 MB

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res, stack = [], []

        def rec_func(opened, closed):
            if opened == closed == n:
                res.append("".join(stack))
                return
            if opened < n:
                stack.append("(")
                rec_func(opened+1, closed)
                stack.pop()
            if closed < opened:
                stack.append(")")
                rec_func(opened, closed+1)
                stack.pop()

        rec_func(0, 0)
        return res
