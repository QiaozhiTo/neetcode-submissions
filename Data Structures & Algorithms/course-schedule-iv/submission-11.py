class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        adj = defaultdict(list)
        for a, b in prerequisites:
            adj[b].append(a)
        
        preMap = {}
        def dfs(crs):
            if crs not in preMap:
                preMap[crs] = set()
                for nei in adj[crs]:
                    preMap[crs] |= dfs(nei)
                preMap[crs].add(crs)
            return preMap[crs]
            
        res = []
        for u, v in queries:
            res.append(u in dfs(v))
        return res