class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        direction = [[0,1], [0, -1], [1, 0], [-1, 0]]
        area = 0
        visit = set()

        def bfs(r, c):
            q = deque([(r, c)])
            visit.add((r, c))
            res = 1
            while q:
                row, col  = q.popleft()
                for dr, dc in direction:
                    nr, nc = dr + row, dc + col
                    if (nr in range(rows) and nc in range(cols) and grid[nr][nc] == 1 and (nr, nc) not in visit):
                        q.append((nr, nc))
                        visit.add((nr,nc))
                        res += 1
            return res

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and (r, c) not in visit:
                    area = max(area, bfs(r, c))
        return area
