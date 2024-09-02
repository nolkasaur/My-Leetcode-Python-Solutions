# https://leetcode.com/problems/group-anagrams/
# 87 ms, 19.3 MB

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = {}
        for s in strs:
            sorted_s = "".join(sorted(s))
            if sorted_s in hashmap:
                hashmap[sorted_s].append(s)
            else:
                hashmap[sorted_s] = [s]
        return hashmap.values()
