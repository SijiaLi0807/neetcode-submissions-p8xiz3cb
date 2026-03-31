# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]: 
        head = list3 = ListNode() #listnode是不可迭代的对象，所以是赋值而不是指向同一个地址

        while list1 and list2:
            if list1.val < list2.val:
                list3.next = list1
                list1, list3 = list1.next, list3.next
            elif list1.val >= list2.val:   
                list3.next = list2
                list2, list3 = list2.next, list3.next
                
        if list1:
            list3.next = list1
        if list2:
            list3.next = list2
        return head.next
            

        