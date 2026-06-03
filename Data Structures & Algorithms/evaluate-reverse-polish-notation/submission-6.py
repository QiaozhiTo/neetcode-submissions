class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token in '+-*/':
                a, b = int(stack.pop()), int(stack.pop())
                if token == '-':
                    stack.append(b - a)
                elif token == '+':
                    stack.append(a + b)
                elif token == '*':
                    stack.append(a*b)
                else:
                    stack.append(b / a)
            else:
                stack.append(int(token))
        return int(stack[-1])