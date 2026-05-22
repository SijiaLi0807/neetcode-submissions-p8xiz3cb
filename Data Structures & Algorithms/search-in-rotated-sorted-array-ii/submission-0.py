class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        n = len(nums)
        #if n == 1:

        l, r = 0, n-1
        '''
        [5,1,2,3,4]
        [4,5,1,2,3]
        
        '''
        while l <= r:
            m = (l+r)//2
            if nums[m] == target:
                return True

            if nums[l] == nums[m]:
                l+=1
            elif nums[l] < nums[m]:
                if nums[l] <= target < nums[m]: #不需要m=target因为已经判断过
                    r = m-1 
                else:
                    l = m+1
            else:
                if nums[m] < target <= nums[r]:
                    l = m+1
                else:
                    r = m-1
        return False