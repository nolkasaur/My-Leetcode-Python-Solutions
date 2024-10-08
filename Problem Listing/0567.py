# https://leetcode.com/problems/permutation-in-string/
# 65 ms, 16.55 MB

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2): return False
        hashmap_count_s1, hashmap_count_s2 = {}, {}
        left, right = 0, len(s1)-1
        for i in range(len(s1)):
            hashmap_count_s1[s1[i]] = hashmap_count_s1.get(s1[i], 0) + 1
            hashmap_count_s2[s2[i]] = hashmap_count_s2.get(s2[i], 0) + 1
        while right < len(s2):
            if hashmap_count_s1 == hashmap_count_s2:
                return True
            elif right == len(s2)-1:
                return False
            else:
                hashmap_count_s2[s2[left]] -= 1
                if hashmap_count_s2[s2[left]] == 0:
                    hashmap_count_s2.pop(s2[left])
                left += 1
                right += 1
                hashmap_count_s2[s2[right]] = hashmap_count_s2.get(s2[right], 0) + 1
        return False
