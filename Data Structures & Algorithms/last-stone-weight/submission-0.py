class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        #因为python只支持小顶堆，所以在入堆的时候我们要添加的是数据的相反数
        heap = [-stone for stone in stones]
        heapq.heapify(heap)

        while len(heap)>1:
            y = heapq.heappop(heap)
            x = heapq.heappop(heap)
            if x !=y:
                heapq.heappush(heap,y-x)
        if heap:
            return -heap[0]
        return 0