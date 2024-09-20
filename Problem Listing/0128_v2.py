# https://leetcode.com/problems/longest-consecutive-sequence/
# 345 ms, 31.85 MB

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        res = 0
        for n in num_set:
            if n-1 not in num_set: #start of seq
                length = 0
                while n+length in num_set:
                    length+=1
                res = max(res, length)

        return res
