class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        preMap = {i : [] for i in range(numCourses)}
        for crs, pre in prerequisites:
            preMap[crs].append(pre)

        circle = set()
        visit = set()
        output = []
        def dfs(crs):
            if crs in circle:
                return False
            if crs in visit:
                return True

            circle.add(crs)
            for pre in preMap[crs]:
                if dfs(pre) == False:
                    return False
            circle.remove(crs)
            visit.add(crs)
            output.append(crs)
        for c in range(numCourses):
            if dfs(c) == False:
                return []
        return output
