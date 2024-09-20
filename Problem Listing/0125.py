# https://leetcode.com/problems/valid-palindrome/
# 54 ms, 21.81 MB

class Solution:
    def isPalindrome(self, s: str) -> bool:
        #s = "".join(s.split())
        s = "".join(c.lower() for c in s if c.isalnum())
        for i in range(int(len(s)/2)):
            if s[i] != s[len(s)-1-i]:
                return False
        return True
