class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        l, r = 0, len(people)-1
        ans = 0
        people.sort()
        while r >= l:
            if people[r] + people[l] <= limit:
                l+=1
            ans += 1
            r -=1

        return ans
