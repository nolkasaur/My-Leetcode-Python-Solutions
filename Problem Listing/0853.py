# https://leetcode.com/problems/car-fleet/
# 668 ms, 36.06 MB

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairs = [[pos, speed] for pos, speed in zip(position, speed)]
        stack = []
        pairs.sort(key=lambda val : val[0], reverse=True)
        for pos, speed in pairs:
            stack.append((target-pos) / speed)
            if len(stack) > 1 and stack[-1] <= stack[-2]:
                stack.pop()
        return len(stack)
