class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x:x[0])
        res = 0
        prevend = intervals[0][1]
        for start, end in intervals[1:]:
            if prevend > start:
                res += 1
                prevend = min(prevend, end)
            else:
                prevend = end
        return res

