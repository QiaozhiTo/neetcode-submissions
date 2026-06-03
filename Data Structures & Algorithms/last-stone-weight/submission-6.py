class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxHeap = [-s for s in stones]
        heapq.heapify(maxHeap)
        while len(maxHeap) >= 2:
            stone1 = heapq.heappop(maxHeap)
            stone2 = heapq.heappop(maxHeap)
            if stone1 - stone2:
                heapq.heappush(maxHeap, stone1 - stone2)
        return -maxHeap[0] if maxHeap else 0