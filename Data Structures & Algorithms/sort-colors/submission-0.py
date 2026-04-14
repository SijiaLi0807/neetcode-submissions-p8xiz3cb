class Solution:
    def mergesort(self, nums, l, r):
        if l == r:
            return
        mid = (l+r)//2
        self.mergesort(nums,l,mid)
        self.mergesort(nums,mid+1, r)
        tmp = []
        i, j = l, mid +1 
        while i <= mid or j <= r:
            if i > mid or (j <=r and nums[j] < nums[i]):
                tmp.append(nums[j])
                j += 1
            else:
                tmp.append(nums[i])
                i += 1
        nums[l:r+1] = tmp


    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        self.mergesort(nums,0,len(nums)-1)