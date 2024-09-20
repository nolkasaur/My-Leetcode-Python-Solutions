# https://leetcode.com/problems/valid-parentheses/
# 30 ms, 16.60 MB

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        hash_map = {')':'(', '}':'{', ']':'['}
        for char in s:
            if char in hash_map:
                try:
                    if stack[-1] == hash_map[char]:
                        stack.pop()
                    else:
                        return False
                except:
                    return False
            else:
                stack.append(char)
        return not stack
