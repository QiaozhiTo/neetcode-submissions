class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows, cols = len(grid), len(grid[0])
        visit = set()
        q = deque()

        def addroom(r,c):
            if (r < 0 or c < 0 or r == rows or c == cols or (r, c) in visit or grid[r][c] == -1):
                return 
            visit.add((r, c))
            q.append((r,c))

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    q.append((r,c))
                    visit.add((r,c))
        dist = 0 
        while q:
            for i in range(len(q)):
                row, col = q.popleft()
                grid[row][col] = dist
                addroom(row, col+1)
                addroom(row, col-1)
                addroom(row+1, col)
                addroom(row-1, col)
            dist += 1


        