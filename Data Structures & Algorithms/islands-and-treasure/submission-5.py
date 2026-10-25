# class Solution:
#     def islandsAndTreasure(self, grid: List[List[int]]) -> None:
#         rows, cols = len(grid), len(grid[0])
#         q = deque()
#         visit = set()
#         def bfs(r, c):
#             if r not in range(rows) or c not in range(cols) or grid[r][c] == -1 or (r, c) in visit:
#                 return 
#             q.append((r, c))
#             visit.add((r, c))
#         for r in range(rows):
#             for c in range(cols):
#                 if grid[r][c] == 0:
#                     q.append((r, c))
#                     visit.add((r, c))
#         dist = 0
#         while q:
#             for i in range(len(q)):
#                 r, c = q.popleft()
#                 grid[r][c] = dist
#                 bfs(r, c + 1)
#                 bfs(r, c - 1)
#                 bfs(r + 1, c)
#                 bfs(r - 1, c)

#             dist += 1
        

# class Solution:
#     def islandsAndTreasure(self, grid: List[List[int]]) -> None:
#         rows, cols = len(grid), len(grid[0])
#         directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
#         INF = 2147483647
#         visit = set()

#         def bfs(r, c):
#             q = deque([(r, c)])
#             visit = [[False] * cols for _ in range(rows)]
#             visit[r][c] = True
#             steps = 0
#             while q:
#                 for _ in range(len(q)):
#                     row, col = q.popleft()
#                     if grid[row][col] == 0:
#                         return steps
#                     for dr, dc in directions:
#                         nr, nc = dr + row, dc + col
#                         # 能够visit的条件还要注意不是-1，所以要不能直接append
#                         if nr in range(rows) and nc in range(cols) and not visit[nr][nc] and grid[nr][nc] != -1:
#                             visit[nr][nc] = True
#                             q.append((nr, nc))

#                 steps += 1
#             return INF
#         for r in range(rows):
#             for c in range(cols):
#                 if grid[r][c] == INF:
#                     grid[r][c] = bfs(r, c)

       

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows, cols = len(grid), len(grid[0])
        visit = set()
        q = deque()

        def bfs(r, c):
            if r not in range(rows) or c not in range(cols) or grid[r][c] == -1 or (r, c) in visit:
                return 
            q.append((r, c))
            visit.add((r, c))

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    q.append((r, c))
                    visit.add((r, c))
                    
        dist = 0
        while q:
            for _ in range(len(q)):
                row, col = q.popleft()
                grid[row][col] = dist
                bfs(row + 1, col)
                bfs(row, col + 1)
                bfs(row, col - 1)
                bfs(row - 1, col)
            dist += 1


