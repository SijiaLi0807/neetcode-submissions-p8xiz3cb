class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        edges = collections.defaultdict(list)
        indeg = [0] * numCourses # in-degree of node v (入度数组)
        for info in prerequisites:
            edges[info[1]].append(info[0]) # info[1] -> info[0] 
            # if we want to take info[0], we need to take info[1] first.
            indeg[info[0]] += 1 

        q = collections.deque([ u for u in range(numCourses) if indeg[u] == 0])
        res = []
        visited = 0 # store the size of indeg == 0's nodes to determine T/F
        while q:
            visited +=1
            u = q.popleft()
            res.append(u)
            for v in edges[u]:
                indeg[v] -= 1
                if not indeg[v]:
                    q.append(v)
        if len(res) != numCourses:
            res = list()
        return res