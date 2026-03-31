class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        n = len(hand)
        if len(hand) % groupSize > 0:
            return False
        hand.sort()
        cnt = Counter(hand)
        for x in hand:
            #x：此时hand中的最小数，必定是一个group的最小数
            if cnt[x] == 0:
                continue
            for num in range(x,x+groupSize):
                if cnt[num] ==0:
                    return False
                cnt[num] -= 1
        return True