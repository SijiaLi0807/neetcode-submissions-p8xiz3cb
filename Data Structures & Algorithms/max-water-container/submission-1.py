class Solution:
    def maxArea(self, height: List[int]) -> int:
        ans = 0
        i,j= 0, len(height)-1
        while i <= j:
            if height[i] > height[j]:
                res = (j-i)*height[j]
                j-=1
            else:
                res = (j-i)*height[i]
                i+=1
            ans = max(ans, res)
        return ans