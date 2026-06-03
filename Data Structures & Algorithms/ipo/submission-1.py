class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        maxHeap = [] # [-profit, capital]
        pair = [[c, p] for c, p in zip(capital, profits)]
        pair.sort(key = lambda t : t[0]) # ordered by c
        i = 0
        for _ in range(k):
            while i < len(pair) and w >= pair[i][0]:
                heapq.heappush(maxHeap, -pair[i][1])
                i += 1
            if not maxHeap:
                break
            w += -heapq.heappop(maxHeap)
        return w
