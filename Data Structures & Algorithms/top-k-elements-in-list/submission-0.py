class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        times = Counter(nums)
        arr = []
        for num, time in times.items():
            arr.append([time,num])
        arr.sort()
        res = []
        n = len(arr)
        for i in range(k):
            res.append(arr[len(arr)-1-i][1])
        return res


        