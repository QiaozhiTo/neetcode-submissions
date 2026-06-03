class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        adj = collections.defaultdict(list)
        for u, v in prerequisites:
            adj[v].append(u)
        
        def dfs(crs):
            
            if crs not in prereqMap:
                prereqMap[crs] = set()
                for pre in adj[crs]:
                    prereqMap[crs].update(dfs(pre))
                prereqMap[crs].add(crs)

            return prereqMap[crs]
        
        prereqMap = {}
        for crs in range(numCourses):
            dfs(crs)
        res = []
        for u, v in queries:
            res.append(u in prereqMap[v])
        return res
