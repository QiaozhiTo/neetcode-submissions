# class Solution:
#     def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
#         # dfs
#         rows, cols = len(grid), len(grid[0])
#         area = 0

#         def dfs(r, c):
#             if r not in range(rows) or c not in range(cols) or grid[r][c] == 0:
#                 return 0
#             grid[r][c] = 0
#             return 1 + dfs(r, c + 1) + dfs(r, c - 1) + dfs(r + 1, c) + dfs(r - 1, c)

#         for r in range(rows):
#             for c in range(cols):
#                 if grid[r][c] == 1:
#                     area = max(area, dfs(r, c))
#         return area

# class Solution:
#     def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
#         # dfs  
#         rows, cols = len(grid), len(grid[0])
#         area = 0

#         def dfs(r, c):
#             if r in range(rows) and c in range(cols) and grid[r][c] == 1:
#                 grid[r][c] = 0
#                 return 1 + dfs(r, c + 1) + dfs(r, c - 1) + dfs(r + 1, c) + dfs(r - 1, c)
#             return 0

#         for r in range(rows):
#             for c in range(cols):
#                 area = max(area, dfs(r, c))
#         return area

# bfs

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        # BFS
        rows, cols = len(grid), len(grid[0])
        directions = {(1, 0), (0, -1), (0, 1), (-1, 0)}
        area = 0
        q = deque()


        def bfs(r, c):
            res = 1
            grid[r][c] = 0
            q.append((r, c))
            while q:
                row, col = q.popleft()
                for dr, dc in directions:
                    nr, nc = dr + row, dc + col
                    if (nr < 0 or nc < 0 or nr >= rows or nc >= cols or grid[nr][nc] == 0):
                        continue
                    q.append((nr, nc))
                    grid[nr][nc] = 0
                    res += 1
            return res

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    area = max(area, bfs(r, c))
        return area

