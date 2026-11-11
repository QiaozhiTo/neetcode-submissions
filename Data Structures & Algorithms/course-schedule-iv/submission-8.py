class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        adj = {i:[] for i in range(numCourses)}
        for u, v in prerequisites:
            adj[v].append(u)
        
        res = []
        preMap = {}
        def dfs(crs):
            if crs not in preMap:
                preMap[crs] = set()
                for nei in adj[crs]:
                    preMap[crs] |= dfs(nei)
                preMap[crs].add(crs)
            return preMap[crs]

        for u, v in queries:
            res.append(u in dfs(v))
        return res

        