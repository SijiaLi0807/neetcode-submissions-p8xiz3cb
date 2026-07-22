class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        ispre = [[0]*numCourses for _ in range(numCourses)]
        indeg = [0]*numCourses
        edges = collections.defaultdict(list)

        for info in prerequisites:
            ispre[info[0]][info[1]] = 1 
            # if we want to take info[1], we need to take info[0] first.
            indeg[info[1]] += 1 
            edges[info[0]].append(info[1])

        q = collections.deque([u for u in range(numCourses) if indeg[u] == 0])
        while q:
            u = q.popleft()
            for edge in edges[u]:
                indeg[edge]-=1
                if not indeg[edge]:
                    q.append(edge)
                for course in range(numCourses):
                    if ispre[course][u]:
                        ispre[course][edge] = 1

        ans = []
        for query in queries:
            if ispre[query[0]][query[1]]:
                ans.append(True)
            else: 
                ans.append(False)

        return ans


