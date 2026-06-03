# dfs
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        visit = [False] * n
        adj = collections.defaultdict(list)
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        def dfs(node):
            for nei in adj[node]:
                if not visit[nei]:
                    visit[nei] = True
                    dfs(nei)
        res = 0
        for i in range(n):
            if not visit[i]:
                visit[i] = True
                dfs(i)
                res += 1
        return res

        
# union find
# class Solution:
#     def countComponents(self, n: int, edges: List[List[int]]) -> int:
        