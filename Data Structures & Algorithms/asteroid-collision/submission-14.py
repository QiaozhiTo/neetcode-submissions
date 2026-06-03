class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for ast in asteroids:
            while stack and ast < 0 and stack[-1] > 0:
                diff = stack[-1] + ast
                if diff > 0:
                    ast = 0
                elif diff < 0:
                    stack.pop()
                else:
                    ast = 0
                    stack.pop()
            if ast:
                stack.append(ast)
        return stack
