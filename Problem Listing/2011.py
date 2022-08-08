# https://leetcode.com/problems/final-value-of-variable-after-performing-operations/
# 114 ms, 13.9 MB

class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        i = 0
        for x in range(len(operations)):
            if operations[x][1] == '+':
                i+=1
            else:
                i-=1
        return i
