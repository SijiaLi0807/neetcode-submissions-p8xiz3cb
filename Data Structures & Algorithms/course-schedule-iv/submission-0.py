class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        ispre = [[0]*numCourses for _ in range(numCourses)]
        indeg = [0]*numCourses

        for info in prerequisites:
            ispre[info[0]][info[1]] = 1 
            # if we want to take info[1], we need to take info[0] first.
            indeg[info[1]] += 1 

        q = collections.deque([u for u in range(numCourses) if indeg[u] == 0])
        while q:
            u = q.popleft()
            for i in range(numCourses):
                if ispre[u][i]:
                    indeg[i] -= 1
                    if not indeg[i]:
                        q.append(i)
                    for j in range(numCourses):
                        if ispre[j][u]:
                            ispre[j][i] = 1
        ans = []
        for query in queries:
            if ispre[query[0]][query[1]]:
                ans.append(True)
            else: 
                ans.append(False)

        return ans

