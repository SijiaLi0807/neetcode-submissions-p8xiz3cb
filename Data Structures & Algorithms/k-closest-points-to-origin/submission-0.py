class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        res = []
        n = len(points)
        for i in range(n):
            res.append([points[i][0]**2+points[i][1]**2,points[i]]) 
            
        res.sort()
        ans = [i for _, i in res[:k]]
        return ans[:k]    