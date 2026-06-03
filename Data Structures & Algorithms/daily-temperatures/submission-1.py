class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures) 
        stack = []
        for i, val in enumerate(temperatures):
            while stack and val > stack[-1][0]:
                stackVal, index = stack.pop()

                    # res.append(i - index)
                res[index] = i - index
            stack.append([val, i])
        return res