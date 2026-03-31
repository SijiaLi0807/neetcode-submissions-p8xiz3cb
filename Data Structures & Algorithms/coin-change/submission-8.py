class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        n = len(coins)
        ans = [0] + [amount]*amount
        #因为后面是min，所以初始化要用大值
        tmp = 0
        for coin in coins:
            if amount%coin ==0:
                tmp+=1
            for i in range(1, amount + 1):             
                if i - coin >= 0:  
                    ans[i] = min(ans[i],ans[i-coin] + 1)
        
        if tmp == 0 and ans[amount] == amount:
            return -1
        return ans[amount]