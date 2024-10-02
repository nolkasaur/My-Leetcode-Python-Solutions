# https://leetcode.com/problems/plus-one/
# 38 ms, 16.52 MB

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits.reverse()
        for i in range(len(digits)):
            if digits[i] < 9:
                digits[i] += 1
                break
            else:
                digits[i] = 0
        if digits[0] == 0 and digits[len(digits)-1] == 0:
            digits.append(1)
        return reversed(digits)
