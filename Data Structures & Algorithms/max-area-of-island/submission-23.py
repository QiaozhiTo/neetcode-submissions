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

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        # dfs
        rows, cols = len(grid), len(grid[0])
        area = 0

        def dfs(r, c):
            if r  in range(rows) and c in range(cols) and grid[r][c] == 1:
                grid[r][c] = 0
                return 1 + dfs(r, c + 1) + dfs(r, c - 1) + dfs(r + 1, c) + dfs(r - 1, c)
            return 0


        for r in range(rows):
            for c in range(cols):
                area = max(area, dfs(r, c))
        return area