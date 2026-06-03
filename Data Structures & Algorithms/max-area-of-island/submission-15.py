class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        directions = [[1, 0], [-1, 0], [0, 1], [0,-1]]
        visit = set()
        area = 0

        def bfs(r, c):
            q = deque([(r, c)])
            visit.add((r, c))
            res = 1
            while q:
                for i in range(len(q)):
                    row, col = q.popleft()
                    for dr, dc in directions:
                        nr, nc = dr + row, dc + col
                        if (nr < 0 or nc < 0 or nr == rows or nc == cols or (nr, nc) in visit or grid[nr][nc] == 0):
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