class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        res = ""
        maxHeap = []
        for count, char in [(-a, "a"), (-b, "b"), (-c, "c")]:
            if count:
                heapq.heappush(maxHeap, [count, char])
        
        while maxHeap:
            cnt, char = heapq.heappop(maxHeap)
            if len(res) > 1 and res[-1] == res[-2] == char:
                if not maxHeap:
                    break
            
                cnt2, char2 = heapq.heappop(maxHeap)
                cnt2 += 1
                res += char2
                if cnt2:
                    heapq.heappush(maxHeap, [cnt2, char2])
                heapq.heappush(maxHeap, [cnt, char])

            else:
                cnt += 1
                res += char
                if cnt:
                    heapq.heappush(maxHeap, [cnt, char])
        return res



