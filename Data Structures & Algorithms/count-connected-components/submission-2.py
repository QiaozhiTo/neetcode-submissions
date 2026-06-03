# class Solution:
#     def countComponents(self, n: int, edges: List[List[int]]) -> int:
#         par = [i for i in range(n)]
#         rank = [1] * n

#         def find(n):
#             res = n 
#             while res != par[res]:
#                 par[res] = par[par[res]]
#                 res = par[res]
#             return res
        
#         def union(n1, n2):
#             p1, p2 = find(n1), find(n2)
#             if p1 == p2:
#                 return 0
#             if rank[p1] >= rank[p2]:
#                 par[p2] = p1
#                 rank[p1] += rank[p2]
#             else:
#                 par[p1] = p2
#                 rank[p2] += rank[p1]
#             return 1
#         res = n
#         for n1, n2 in edges:
#             res -= union(n1, n2)
#         return res

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = collections.defaultdict(list)
        visit = [False] * n
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        def dfs(n):
            for nei in adj[n]:
                if not visit[nei]:
                    visit[nei] = True
                    dfs(nei)
        res = 0
        for node in range(n):
            if not visit[node]:
                visit[node] = True
                dfs(node)
                res += 1   
        return res               