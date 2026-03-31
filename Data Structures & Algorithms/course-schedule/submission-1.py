class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        edges = collections.defaultdict(list)
        '''
        edges looks like:
{
    0: [1, 2],
    1: [3],
    2: [3]
} 
        '''
        # vs dict()
        #defaultdict(list)的默认值类型是 list。
        #即当你访问一个还不存在的键时，它不会报错，而是自动先创建一个空列表 []。
        #第一次写 edges[1].append(2) 时，edges[1] 原本不存在。
        #但 defaultdict(list) 会自动把 edges[1] 变成 []。然后再执行 .append(2)
        indeg = [0] * numCourses # in-degree of node v (入度数组)
        for info in prerequisites:
            edges[info[1]].append(info[0]) # info[1] -> info[0] 
            # if we want to take info[0], we need to take info[1] first.
            indeg[info[0]] += 1 

        q = collections.deque([ u for u in range(numCourses) if indeg[u] == 0])
        # deque: first in first out
        # Puts all courses with no prerequisites into the queue first.

        visited = 0 # store the size of indeg == 0's nodes to determine T/F
        while q:
            visited +=1
            u = q.popleft()
            for v in edges[u]:
                # after we remove u from the graph, v has -1 prerequisite.
                indeg[v] -= 1
                if not indeg[v]:
                    q.append(v)

        return visited == numCourses 