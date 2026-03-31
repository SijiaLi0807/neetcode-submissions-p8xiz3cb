class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1  #此时是左闭右开，因为永远拿右边比
        while left < right:  
            mid = (left+right)//2
            if nums[mid]<nums[-1]:
                right = mid
            else: #x≤nums[n−1]
            #x 要么是最小值，要么在最小值右边。
                
                left = mid+1
            #if left == right:
            #    return left
        return nums[left]