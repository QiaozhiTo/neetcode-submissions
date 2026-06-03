class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        preMap = {i :[] for i in range(numCourses)}
        for crs, pre in prerequisites:
            preMap[crs].append(pre)
        circle = set()
        visit = set()
        res = []
        def dfs(crs):
            if crs in visit:
                return True
            if crs in circle:
                return False
            circle.add(crs)
            for pre in preMap[crs]:
                if dfs(pre) == False :
                    return False
            circle.remove(crs)
            visit.add(crs)
            res.append(crs)
            return True
        for crs in range(numCourses):
            if  dfs(crs) == False:
                return []
        return res