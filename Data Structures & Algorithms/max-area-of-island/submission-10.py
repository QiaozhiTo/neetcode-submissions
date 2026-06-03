class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        area = 0 
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        # visit= set()


        def bfs(r, c):
            q = deque([(r, c)])
            visit= set([(r, c)])
            res = 1

            while q:
                 
                row, col = q.popleft()
                for dr, dc in directions:
                    nr, nc = row + dr, col + dc
                    if ( nr in range(rows) and nc in range(cols) and grid[nr][nc] == 1 and (nr, nc) not in visit):
                        q.append((nr, nc))
                        visit.add((nr, nc))
                        res += 1
            return res
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 :

                    area = max(area, bfs(r,c))
        return area

        