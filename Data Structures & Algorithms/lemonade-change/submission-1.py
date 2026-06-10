class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        five = 0
        ten = 0
        for bill in bills:
            if bill == 5:
                five+=1
            if bill == 10:
                if not five:
                    return False
                five-=1
                ten+=1
            if bill == 20:
                if five and ten:
                    five-=1
                    ten-=1
                elif five > 2:
                    five-=3
                else:
                    return False
        return True 