# https://leetcode.com/problems/k-closest-points-to-origin/
# 85 ms, 22.20 MB

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        aux_list = [[p[0] ** 2 + p[1] ** 2, p[0], p[1]] for p in points]
        heapq.heapify(aux_list)
        res = []
        for i in range(k):
            aux_sub_list = heapq.heappop(aux_list)
            res.append([aux_sub_list[1], aux_sub_list[2]])
        return res
