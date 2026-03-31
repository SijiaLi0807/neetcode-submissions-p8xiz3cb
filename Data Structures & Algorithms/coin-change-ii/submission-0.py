class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins)
        ans = [1] + [0] * amount

        for coin in coins:
            for i in range(1, amount + 1): 
                if i - coin >= 0:    
                    ans[i] += ans[i-coin]
        return ans[amount]
        