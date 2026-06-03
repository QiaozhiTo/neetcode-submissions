class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) > n - 1:
            return False
        adj = {i : [] for i in range(n)}
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)
        visit = set()
        def dfs(node, prev):
            if node in visit:
                return False
            visit.add(node)
            for nei in adj[node]:
                if nei == prev:
                    continue
                if not dfs(nei, node):
                    return False
            return True
        return dfs(0, -1) and len(visit) == n
