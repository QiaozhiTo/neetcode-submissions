class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        adj = {i : [] for i in range(numCourses)}
        # adj = collections.defaultdict(list)
        for a, b in prerequisites:
            adj[b].append(a)

        def dfs(crs):
            if crs not in preMap:
                preMap[crs] = set()
                for nei in adj[crs]:
                    preMap[crs].update(dfs(nei))
                preMap[crs].add(crs)
            return preMap[crs]

        preMap = {}
        for n in range(numCourses):
            dfs(n)
        res = []
        for u, v in queries:
            res.append(u in preMap[v])
        return res


        
        