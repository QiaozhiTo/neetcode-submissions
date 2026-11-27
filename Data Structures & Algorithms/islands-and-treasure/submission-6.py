"""
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows, cols = len(grid), len(grid[0])
        
        q = deque()
        visited= set()

        def bfs(r, c):
            if r not in range(rows) or c not in range(cols) or grid[r][c] == -1 or (r, c) in visited:
                return 
            visited.add((r, c))
            q.append((r, c))

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    q.append([r, c])
                    visited.add((r, c))

        dist = 0
        while q:
            for i in range(len(q)):
                r, c = q.popleft()
                grid[r][c] = dist
                bfs(r + 1, c)
                bfs(r - 1, c)           
                bfs(r, c + 1)          
                bfs(r, c - 1)           
            dist += 1
"""
'''
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows, cols = len(grid), len(grid[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        visit = set()
        INF = 2147483647

        def bfs(r, c):
            q = deque([(r, c)])
            visit = [[False] * cols for _ in range(rows)]
            visit[r][c] = True 
            step = 0

            while q:
                for _ in range(len(q)):
                    row, col = q.popleft()
                    if grid[row][col] == 0:
                        return step
                    for dr, dc in directions:
                        nr, nc = row + dr, col + dc
                        if nr in range(rows) and nc in range(cols) and visit[nr][nc] == False and grid[nr][nc] != -1:
                            
                            q.append((nr, nc))
                            visit[nr][nc] = True 
                step += 1
            return INF



        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == INF:
                    grid[r][c] = bfs(r, c)
'''
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows, cols = len(grid), len(grid[0])
        visit = set()
        q = deque()

        def bfs(r, c):
            if r < 0 or r == rows or c < 0 or c == cols or (r, c) in visit or grid[r][c] == -1:
                return 
            q.append((r, c))
            visit.add((r, c))
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0 and (r, c) not in visit:
                    q.append((r, c))
                    visit.add((r, c))
        dist = 0
        while q:
            for i in range(len(q)):
                r, c = q.popleft()
                grid[r][c] = dist
                bfs(r, c + 1)
                bfs(r, c - 1)
                bfs(r + 1, c)
                bfs(r - 1, c)

            dist += 1
