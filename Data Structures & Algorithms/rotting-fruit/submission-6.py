class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # count fresh
        # time
        # return time if not fresh, else -1
        # BFS, q = deque(), while q and fresh > 0
        fresh, time = 0, 0 
        rows, cols = len(grid), len(grid[0])
        q = deque()

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    q.append((r, c))
                elif grid[r][c] == 1:
                    fresh += 1
        while q and fresh > 0:
            for _ in range(len(q)):
                row, col = q.popleft()
                for dr, dc in [[1,0], [-1, 0], [0, 1], [0, -1]]:
                    r, c = row + dr, col + dc
                    if r in range(rows) and c in range(cols) and grid[r][c] == 1:
                        grid[r][c] = 2
                        fresh -= 1
                        q.append((r, c))
            time += 1
        return time if not fresh else -1