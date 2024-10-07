# https://leetcode.com/problems/longest-substring-without-repeating-characters/
# 55 ms, 16.56 MB

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res, ss_len, left, right, hashset = 0, 1, 0, 1, set()
        if len(s) == 0: return 0
        if len(s) == 1: return 1
        hashset.add(s[0])
        while right < len(s):
            if s[right] in hashset:
                hashset.remove(s[left])
                left += 1
                if ss_len > res: res = ss_len
                ss_len -= 1
            else:
                hashset.add(s[right])
                ss_len += 1
                right += 1
        return max(res, ss_len)
