# https://leetcode.com/problems/letter-combinations-of-a-phone-number/
# 0 ms, 16.67 MB

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        char_mapping = {
                    "2": "abc",
                    "3": "def",
                    "4": "ghi",
                    "5": "jkl",
                    "6": "mno",
                    "7": "pqrs",
                    "8": "tuv",
                    "9": "wxyz"
                    }
        res = []
        def backtrack(i, curr_str):
            if i>= len(digits):
                res.append(curr_str)
                return
            for c in char_mapping[digits[i]]:
                backtrack(i + 1, curr_str + c)
        if digits:
            backtrack(0, "")
        return res
