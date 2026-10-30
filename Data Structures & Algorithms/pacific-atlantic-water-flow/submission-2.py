class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pac, atl = set(), set()
        rows, cols = len(heights), len(heights[0])

        def dfs(visit, r, c, prevHeight):
            if ((r, c) in visit or r < 0 or c < 0 or r == rows or c == cols or heights[r][c] < prevHeight):
                return 
            visit.add((r, c))
            dfs(visit, r, c + 1, heights[r][c])
            dfs(visit, r, c - 1, heights[r][c])
            dfs(visit, r + 1, c, heights[r][c])
            dfs(visit, r - 1, c, heights[r][c])

        for r in range(rows):
            dfs(pac, r, 0, heights[r][0])
            dfs(atl, r, cols - 1, heights[r][cols - 1])
        for c in range(cols):
            dfs(pac, 0, c, heights[0][c])
            dfs(atl, rows - 1, c, heights[rows - 1][c])

        res = []
        for r in range(rows):
            for c in range(cols):
                if (r, c) in pac and (r, c) in atl:
                    res.append([r, c])
        return res



        
