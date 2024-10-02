# https://leetcode.com/problems/happy-number/
# 33 ms, 16.95 MB

class Solution:
    def isHappy(self, n: int) -> bool:
        visited = set()
        while n not in visited:
            visited.add(n)
            n = self.AddSquares(n)
            print(n)
        return n == 1
    def AddSquares(self, n: int) -> int:
        res = 0
        while n:
            digit = n%10 # get least significant digit
            digit **= 2 # square the digit
            res += digit # add the squared digit to the output variable
            n //= 10 # floor division to get the number minus the least significant digit
        return res
