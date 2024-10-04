# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/
# 103 ms, 17.78 MB

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left_bound, right_bound = 0, len(numbers)-1
        while True:
            sum = numbers[left_bound] + numbers[right_bound]
            if sum == target:
                return [left_bound + 1, right_bound + 1]
            elif sum > target:
                right_bound -= 1
            else:
                left_bound += 1
