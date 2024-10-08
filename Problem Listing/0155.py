# https://leetcode.com/problems/min-stack/
# 58 ms, 20.62 MB

class MinStack:

    def __init__(self):
        self.stack = []
        self.stack_aux = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if len(self.stack_aux) == 0:
            self.stack_aux.append(val)
        else:
            self.stack_aux.append(min(val, self.stack_aux[-1] if self.stack_aux else val))

    def pop(self) -> None:
        self.stack.pop()
        self.stack_aux.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.stack_aux[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
