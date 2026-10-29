class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # fresh, time
        # when there is no fresh left return time else -1
        
        rows, cols = len(grid), len(grid[0])
        q = deque()
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        time, fresh = 0, 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    q.append((r, c))
                elif grid[r][c] == 1:
                    fresh += 1
        # while fresh > 0
        while q and fresh > 0:
            for _ in range(len(q)):
                r, c = q.popleft()
                for dr, dc in directions:
                    row, col = r + dr, c + dc
                    if row in range(rows) and col in range(cols) and grid[row][col] == 1:
                        fresh -= 1
                        q.append((row, col))
                        grid[row][col] = 2
            time += 1
        return time if fresh == 0 else -1