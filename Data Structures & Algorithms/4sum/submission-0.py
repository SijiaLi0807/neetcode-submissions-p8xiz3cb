class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        n = len(nums)
        ans = []
        if n < 4:
            return ans
        nums.sort()

        for a in range(n-3):
            na = nums[a]
            if a > 0 and na == nums[a-1]:
                continue
            
            for b in range(a+1,n-2):
                nb = nums[b]
                if b > a+1 and nb == nums[b-1]:
                    continue

                d = n-1
                target_val = target - na - nb
                # d 需要在选完a和b后设置，保障每一组新的ab重制后，d都复位了

                for c in range(b+1,n-1):
                    nc = nums[c]
                    if c > b+1 and nc == nums[c-1]:
                        continue

                    while d > c and nc + nums[d] > target_val:
                        d-=1
                    if d == c:
                        break
                    if nums[d] + nc == target_val:
                        ans.append([na,nb,nc,nums[d]]) 
        return ans
