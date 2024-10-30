# https://leetcode.com/problems/palindrome-partitioning/
# 42 ms, 34.01 MB

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res, part = [], []
        def dfs(i):
            if i >= len(s):
                res.append(part.copy())
                return
            for x in range(i, len(s)):
                if self.isPalindrome(s, i, x):
                    part.append(s[i:x+1])
                    dfs(x + 1)
                    part.pop()
        dfs(0)
        return res
    def isPalindrome(self, s, l, r):
        while l < r:
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1
        return True
