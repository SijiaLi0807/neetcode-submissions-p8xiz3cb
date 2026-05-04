from bisect import bisect_left
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        n = len(arr)
        right = bisect_left(arr,x)
        # 在一个已经升序排序的数组 arr 中，找到 x 应该插入的位置，使数组仍然有序；如果数组里已经有 x，返回最左边那个 x 的位置。
        left = right -1 
        for _ in range(k):
            if left < 0:
                right+=1
            elif right >= n:
                left-=1 
            else:
                if x - arr[left] > arr[right] - x:
                    right+=1
                else:
                    left-=1 
        return arr[left+1:right] #左右都不取
        

        
