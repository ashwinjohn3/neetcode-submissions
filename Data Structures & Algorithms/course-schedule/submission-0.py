class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        visiting = set()
        visitedCourses = 0
        # build adjacency list 
        pre_map = defaultdict(list)
        for crs, pre in prerequisites:
            pre_map[crs].append(pre)

        def dfs(course):
            if course in visiting:
                return False
            if pre_map[course] == []:
                return True 
            visiting.add(course)
            for i in pre_map[course]:
                val = dfs(i)
                if not val:
                    return False 
            visiting.remove(course)
            pre_map[course] = []
            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return False
        return True 
            
        