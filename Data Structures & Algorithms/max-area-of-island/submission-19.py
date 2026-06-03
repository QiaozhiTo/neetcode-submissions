class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        directions = [[1,0], [-1, 0], [0, 1], [0, -1]]
        q = deque()
        visit = set()
        area = 0
        rows, cols = len(grid), len(grid[0])

        def bfs(r, c):
            q.append((r, c))
            visit.add((r, c))
            res = 1
            while q:
                for i in range(len(q)):
                    row, col = q.popleft()
                    for dr, dc in directions:
                        nr, nc = dr + row, dc + col
                        # if (nr in range(rows) and nc in range(cols) and (nr, nc) not in visit and grid[nr][nc] == 1):
                        #     q.append((nr, nc))
                        #     visit.add((nr, nc))
                        #     res += 1
                        if (nr not in range(rows) or nc not in range(cols) or (nr, nc) in visit or grid[nr][nc] == 0):
                            continue
                        q.append((nr, nc))
                        visit.add((nr, nc))
                        res += 1
                        
            return res

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and (r, c) not in visit:
                    area = max(area, bfs(r, c))
        return area