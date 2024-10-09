# https://leetcode.com/problems/evaluate-reverse-polish-notation/
# 66 ms, 17.14 MB

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for char in tokens:
            if char == '+':
                stack.append(stack.pop() + stack.pop())
            elif char == '-':
                last, second_last = stack.pop(), stack.pop()
                stack.append(second_last - last)
            elif char == '*':
                stack.append(stack.pop() * stack.pop())
            elif char == '/':
                last, second_last = stack.pop(), stack.pop()
                stack.append((int)(second_last / last))
            else:
                stack.append((int)(char))
        return stack[0]
