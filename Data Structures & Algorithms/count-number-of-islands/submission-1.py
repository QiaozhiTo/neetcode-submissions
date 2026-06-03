class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:return 0
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        rows, cols = len(grid), len(grid[0])
        island = 0 
        visit = set()

        def dfs(r, c):
            q = deque([(r,c)])
            visit.add((r, c))
            while q:
                row,col = q.popleft()
                for dr, dc in directions:
                    nr, nc = row + dr, col+ dc
                    if (nr in range(rows) and nc in range(cols) and 
                        grid[nr][nc] == "1" and (nr, nc) not in visit):
                    
                        visit.add((nr, nc))
                        q.append((nr, nc))

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r, c) not in visit:
                    dfs(r, c)
                    island += 1
        return island