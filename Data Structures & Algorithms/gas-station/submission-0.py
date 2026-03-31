class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        #net = gas - cost
        i = start = cursum =totalsum = 0        
        n = len(gas)
        while i < n: 
            cursum = cursum + gas[i] - cost[i]
            totalsum = totalsum + gas[i] - cost[i]
            if cursum < 0:
                start = i+1
                cursum = 0
            i+=1
        if totalsum <0 :
            return -1
        return start