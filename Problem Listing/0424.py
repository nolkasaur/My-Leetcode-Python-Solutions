# https://leetcode.com/problems/longest-repeating-character-replacement/
# 83 ms, 16.73 MB

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res, left, hashmap_count = 0, 0, {}
        for i in range(len(s)):
            sub_len = i - left + 1
            hashmap_count[s[i]] = hashmap_count.get(s[i], 0) + 1
            if sub_len - max(hashmap_count.values()) > k:
                hashmap_count[s[left]] -= 1
                left += 1
            else:
                if sub_len > res: res = sub_len
        return res
