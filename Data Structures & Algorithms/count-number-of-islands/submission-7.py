class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        rows, cols = len(grid), len(grid[0])
        q = deque()
        visit = set()
        islands = 0

        def bfs(r, c):
            q.append((r, c))
            visit.add((r, c))
            while q:
                for i in range(len(q)):
                    row, col = q.popleft()
                    for dr, dc in directions:
                        nr, nc = dr + row, dc + col
                        if (nr not in range(rows) or nc not in range(cols) or (nr, nc) in visit or grid[nr][nc] == "0"):
                            continue
                        q.append((nr, nc))
                        visit.add((nr, nc)) 
                           

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r, c) not in visit:
                    bfs(r, c)
                    islands += 1
        return islands