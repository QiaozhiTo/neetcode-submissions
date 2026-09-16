# class Solution:
#     def numIslands(self, grid: List[List[str]]) -> int:
#         directions = [[1,0],[-1,0], [0,-1],[0,1]]
#         rows, cols = len(grid), len(grid[0])
#         visit = set()
#         q = deque()
#         islands = 0

#         def bfs(r,c):
#             q.append((r,c))
#             visit.add((r,c))
#             while q:
#                 row, col = q.popleft()
#                 for dr, dc in directions:
#                     nr, nc = dr + row, dc + col
#                     if (nr in range(rows) and nc in range(cols) and (nr,nc) not in visit and grid[nr][nc] == "1"):
#                         q.append((nr, nc))
#                         visit.add((nr, nc))


#         for r in range(rows):
#             for c in range(cols):
#                 if grid[r][c] == "1" and (r, c) not in visit:
#                     bfs(r,c)
#                     islands += 1
#         return islands

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])
        visit = set()
        islands = 0
        def dfs(i, j):
            if i in range(rows) and j in range(cols) and grid[i][j] == "1" and (i, j) not in visit:
                
                visit.add((i, j))
                dfs(i, j + 1)
                dfs(i, j - 1)
                dfs(i + 1, j)
                dfs(i - 1, j)
           

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r, c) not in visit:
                    dfs(r, c)
                    islands += 1
        return islands