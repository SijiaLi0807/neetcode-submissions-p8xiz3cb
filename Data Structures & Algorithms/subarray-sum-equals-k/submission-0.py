class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        cnt = defaultdict(int) #普通 dict：访问不存在的 key 会报错。
        # defaultdict(int)：访问不存在的 key 时，会自动创建这个 key，默认 value 是 0
        ans = s = 0
        cnt[0] = 1
        for n in nums:
            s += n
            ans += cnt[s-k]
            cnt[s] +=1
        return ans

