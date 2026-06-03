class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []
        for index, temp in enumerate(temperatures):
            while stack and stack[-1][1] < temp:
                stackInd, stackTemp = stack.pop()
                res[stackInd] = index - stackInd
            stack.append([index, temp])
        return res
