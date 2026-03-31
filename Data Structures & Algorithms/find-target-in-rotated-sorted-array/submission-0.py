class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        l, r = 0, n - 1 
        while l <= r:
            m = (l+r)//2 #注意，这是向下取整的
            if nums[m] == target: 
                return m
            if nums[m] >= nums[l]: #注意是>=而不是>:边界情况当m==l会出错，因为此时左边只有一个数，应该算有序
            #可以用[3,1]举例
                if target < nums[m] and target >= nums[l]: 
                    r = m - 1
                else:
                    l = m + 1
            else:
                if target <= nums[r] and target > nums[m]:
                    l = m + 1
                else:
                    r = m - 1
        return -1

        
        