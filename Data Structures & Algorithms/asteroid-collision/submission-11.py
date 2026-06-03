class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for each in asteroids:
            while stack and stack[-1] > 0 and each < 0:
                diff = stack[-1] + each
                if diff < 0:
                    stack.pop()
                elif diff > 0:
                    each = 0
                else:
                    each = 0
                    stack.pop()
            if each:
                stack.append(each)
        return stack