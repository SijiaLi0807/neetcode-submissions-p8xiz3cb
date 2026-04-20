class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        cnt = {}
        ans = []
        target = len(nums)//3
        for n in nums:
            if n in cnt:
                cnt[n]+=1
            else:
                cnt[n]=1
        for k in cnt.keys():
            if cnt[k] > target:
                ans.append(k)
        return ans