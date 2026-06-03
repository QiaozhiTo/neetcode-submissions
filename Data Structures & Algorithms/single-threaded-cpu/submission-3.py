class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        for i, t in enumerate(tasks):
            t.append(i)
        tasks.sort(key = lambda t:t[0])
        res = []# index
        maxHeap = []

        i = 0
        time = tasks[0][0]

        while i < len(tasks) or maxHeap:
            while i < len(tasks) and time >= tasks[i][0]:
                heapq.heappush(maxHeap, [tasks[i][1], tasks[i][2]])
                i += 1
            if not maxHeap:
                time = tasks[i][0]
            else:
                procTime, index = heapq.heappop(maxHeap)
                time += procTime
                res.append(index)
        return res