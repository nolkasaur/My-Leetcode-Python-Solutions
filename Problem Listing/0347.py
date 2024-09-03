# https://leetcode.com/problems/top-k-frequent-elements/
# 85 ms, 21.2 MB

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}
        sol_list = []
        for n in nums:
            hashmap[n] = hashmap.get(n, 0) + 1
        sorted_list = sorted(hashmap.items(), key=lambda item: item[1], reverse=True)
        for i in range(k):
            sol_list.append(sorted_list[i][0])
        return sol_list
