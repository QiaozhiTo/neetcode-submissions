class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        visit = set()
        if len(edges) > n - 1:
            return False
        adj = {i : []  for i in range(n)}
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)
        
        def dfs(i, prev):
            if i in visit:
                return False
            visit.add(i)
            for nei in adj[i]:
                if nei == prev:
                    continue
                if not dfs(nei, i):
                    return False
            return True


        return dfs(0, -1) and len(visit) == n
