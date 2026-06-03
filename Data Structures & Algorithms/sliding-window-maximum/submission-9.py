# class Solution:
#     def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
#         l = 0
#         res = []
#         window = {}

#         for r in range(k-1, len(nums)):
#             if r - l + 1 > k:
#                 l += 1
#             res.append(max(nums[l: r + 1]))
#         return res

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = deque()
        res = []
        l = 0
        for r in range(len(nums)):
            while q and nums[q[-1]] < nums[r]:
                q.pop()
            q.append(r)

            if l > q[0]:
                q.popleft()

            if r - l + 1 >= k:
                res.append(nums[q[0]])
                l += 1
        return res
