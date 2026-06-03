class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        area = 0
        visit = set()

        def dfs(r, c):
            q = deque()
            q.append((r,c))
            visit.add((r,c))
            res = 0
            while q:
                res +=1
                row, col = q.popleft()
                direction = [[0,1], [0, -1], [1, 0], [-1, 0]]
                for dr, dc in direction:
                    r = row + dr
                    c = col + dc
                    if (r in range(rows) and c in range(cols) and 
                    grid[r][c] == 1  and (r,c) not in visit):
                        q.append((r,c))
                        visit.add((r,c))
                        # res += 1
            return res
            
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and (r, c) not in visit:
                    area = max(area,  dfs(r,c))
        return area
        
