class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack= []
        for each in tokens:
            if each in ("+", "-", "*", "/"):
                if each == "+":
                    res = stack.pop() + stack.pop()
                if each == "*":
                    res = stack.pop() * stack.pop()
                if each ==  "-":
                    a, b = stack.pop(), stack.pop()
                    res = b - a
                if each == "/":
                    a, b = stack.pop(), stack.pop()
                    res = int(b/a)
                stack.append(res)
            else:
                stack.append(int(each))
        return stack[0]