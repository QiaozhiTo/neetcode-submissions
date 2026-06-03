class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        preMap = {i : [] for i in range(numCourses)}
        for a, b in prerequisites:
            preMap[a].append(b)
        visit, cycle = set(), set()
        res = []
        def dfs(crs):
            if crs in cycle:
                return False
            if crs in visit:
                return True
            
            cycle.add(crs)
            for nei in preMap[crs]:
                if not dfs(nei):
                    return False
            
            cycle.remove(crs)
            visit.add(crs)
            res.append(crs)
            return True
            

        for n in range(numCourses):
            if not dfs(n):
                return []
        return res