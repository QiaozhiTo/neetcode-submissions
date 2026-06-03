class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minHeap = []
        res = []
        for x, y in points:
            dis = x ** 2 + y ** 2
            heapq.heappush(minHeap, (dis, x, y))
        while k > 0:
            dis, x, y = heapq.heappop(minHeap)
            res.append([x, y])
            k -= 1
        return res
        