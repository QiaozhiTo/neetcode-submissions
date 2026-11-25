class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        par = [i for i in range(n)]
        rank = [1] * n
        def find(n):
            while n != par[n]:
                par[n] = par[par[n]]
                n = par[n]
            return n 
        
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
            return 1 #unconnected part


        res = n
        for a, b in edges:
            res -= union(a, b)
        return res