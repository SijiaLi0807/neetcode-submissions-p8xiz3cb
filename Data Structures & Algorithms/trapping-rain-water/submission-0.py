class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        leftmax = [height[0]] + [0] * (n-1)
        rightmax = [0] * (n-1) + [height[n-1]]
        #左边遍历一遍
        for i in range(1,n):
            leftmax[i] = max(leftmax[i-1],height[i])
            rightmax[n-i-1] = max(rightmax[n-i],height[n-i-1])
        ans = [0] * n
        #右边遍历一遍
        for i in range(n):
            ans[i] = min(leftmax[i],rightmax[i]) - height[i]
        return sum(ans)

        