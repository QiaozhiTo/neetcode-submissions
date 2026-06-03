class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        preMap = collections.defaultdict(list)
        for crs, pre in prerequisites:
            preMap[crs].append(pre)
        
        res = []

        visit = set()
        circle = set()

        def dfs(crs):
            if crs in circle:
                return False
            if crs in visit:
                return True
            circle.add(crs)
            for pre in preMap[crs]:
                if not dfs(pre):
                    return False
            circle.remove(crs)
            visit.add(crs)
            res.append(crs)
            return res
        for crs in range(numCourses):
            if not dfs(crs):
                return []
        return res
