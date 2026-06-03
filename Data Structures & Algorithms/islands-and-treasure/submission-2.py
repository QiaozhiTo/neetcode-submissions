class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows, cols = len(grid), len(grid[0])
        visit = set()
        q = deque()

        def dfs(r, c):
            if (r < 0 or c < 0 or r == rows or c == cols or grid[r][c] == -1
            or (r, c) in visit):
                return 
            q.append((r, c))
            visit.add((r, c))

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    dfs(r, c)

        dist = 0
        while q:
            for i in range(len(q)):
                row, col = q.popleft()
                grid[row][col] = dist
                dfs(row, col + 1)
                dfs(row, col - 1)
                dfs(row + 1, col)
                dfs(row - 1, col)

            dist += 1