# dfs
# class Solution:
#     def countComponents(self, n: int, edges: List[List[int]]) -> int:
#         visit = [False] * n
#         adj = collections.defaultdict(list)
#         for u, v in edges:
#             adj[u].append(v)
#             adj[v].append(u)

#         def dfs(node):
#             for nei in adj[node]:
#                 if not visit[nei]:
#                     visit[nei] = True
#                     dfs(nei)
#         res = 0
#         for i in range(n):
#             if not visit[i]:
#                 visit[i] = True
#                 dfs(i)
#                 res += 1
#         return res

        
# union find
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        rank = [1] * n
        par = [i for i in range(n)]

        def find(n):
            res = n
            while res != par[res]:
                par[res] = par[par[res]]
                res = par[res]
            return res
        def union(n1, n2):
            p1, p2 = find(n1), find(n2)
            if p1 == p2:
                return 0
            if rank[p1] >= rank[p2]:
                rank[p1] += rank[p2]
                par[p2] = p1
            else:
                rank[p2] += rank[p1]
                par[p1] = p2
            return 1

        res = n
        for n1, n2 in edges:
            res -= union(n1, n2)
        return res        