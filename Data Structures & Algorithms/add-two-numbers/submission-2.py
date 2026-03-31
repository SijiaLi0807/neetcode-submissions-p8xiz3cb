# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        num1, num2 = 0, 0
        i = 0
        while l1:
            num1 = num1 + l1.val*10**i
            l1 = l1.next
            i +=1
        i = 0
        while l2:
            num2 = num2 + l2.val*10**i
            l2 = l2.next
            i +=1
        Sum = num1 + num2
        head = l3 = ListNode(0)
        if Sum ==0:
            return head
        while Sum:
            l3.next = ListNode(Sum%10)
            l3 = l3.next
            Sum = Sum//10
        return head.next
            
        

        