# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        ans = []
        for l in lists:
            while l:
                ans.append(l.val)
                l = l.next
        ans = sorted(ans)
        head = res = ListNode()
        for l in ans:
            res.next = ListNode(l)
            res = res.next
            

        return head.next
        