class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        maxHeap = []
        count = {(-a, 'a'), (-b, 'b'), (-c, 'c')}
        for cnt, char in count:
            if cnt:
                heapq.heappush(maxHeap, [cnt, char])
        res = ""

        while maxHeap:
            cnt, char = heapq.heappop(maxHeap)
            if len(res) > 1 and res[-1] == res[-2] == char:
                if not maxHeap:
                    break
                count2, char2 = heapq.heappop(maxHeap)
                res += char2
                count2 += 1
                if count2:
                    heapq.heappush(maxHeap, [count2, char2])
                heapq.heappush(maxHeap, [cnt, char])
            else:
                cnt += 1
                res += char
                if cnt:
                    heapq.heappush(maxHeap, [cnt, char])
        return res
       