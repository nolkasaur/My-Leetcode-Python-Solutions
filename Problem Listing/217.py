# https://leetcode.com/problems/contains-duplicate/
# 422 ms, 31.9 MB

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashset = set()
        for num in nums:
            if num in hashset:
                return True
            else:
                hashset.add(num)
        return False
