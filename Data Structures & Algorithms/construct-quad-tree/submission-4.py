"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
  
        def dfs(n, r, c):
            allSame = True
            for i in range(n):
                for j in range(n):
                    if grid[r][c] != grid[r+ i][c + j]:
                        allSame = False
                        break
            if allSame:
                return Node(grid[r][c], True)
            
            n = n // 2
            leftTop = dfs(n, r, c)
            rightTop = dfs(n, r, c + n)
            leftBottom = dfs(n, r + n, c)
            rightBottom = dfs(n , r + n, c + n)
            return Node(0, False, leftTop, rightTop, leftBottom, rightBottom)
        return dfs(len(grid), 0, 0)
        