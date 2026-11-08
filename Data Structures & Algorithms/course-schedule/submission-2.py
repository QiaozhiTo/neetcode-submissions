class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # preMap
        preMap = {i : [] for i in range(numCourses)}
        for crs, pre in prerequisites:
            preMap[crs].append(pre)
        # to track the courses you are visiting in the dfs
        visiting = set()
        # def dfs
        def dfs(crs):
            if crs in visiting:
                return False # found a circle
            if preMap[crs] == []:
                return True
            visiting.add(crs)
            for pre in preMap[crs]:
                if not dfs(pre):
                    return False
            preMap[crs] = []
            visiting.remove(crs)
            return True
        for i in range(numCourses):
            if not dfs(i):
                return False
        return True
            
            

        