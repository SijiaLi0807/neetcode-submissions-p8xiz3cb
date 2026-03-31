class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        def dfs(i,cost):
            if i <= 1:
                return 0
            
            return min(dfs(i-1,cost) + cost[i-1], dfs(i-2,cost) + cost[i-2])  
        return dfs(len(cost),cost)
        
