# https://leetcode.com/problems/reverse-string/
# 163 ms, 20.92 MB

class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        for i in range(len(s)//2):
            aux = s[len(s)-1-i]
            s[len(s)-1-i] = s[i]
            s[i] = aux
