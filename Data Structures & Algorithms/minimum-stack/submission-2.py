class MinStack:

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        

    def pop(self) -> None:
        self.stack.pop()
        

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        temp = []
        min_val = self.stack[-1]
        while len(self.stack):
            min_val = min(min_val, self.stack[-1])
            temp.append(self.stack.pop())
        while len(temp):
            self.stack.append(temp.pop())
        return min_val

            
        
