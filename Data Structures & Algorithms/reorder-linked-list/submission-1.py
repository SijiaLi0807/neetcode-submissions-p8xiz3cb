# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def midnode(self, head: Optional[ListNode]) -> ListNode:
        #when fast == None (num of nodes is odd) or fast.next == None (num of nodes is even), loop exits (数学归纳法 mathematical induction 可以证明)
        # then midnode is slow 
        slow = fast = head
        while fast and fast.next: 
            slow, fast = slow.next, fast.next.next
        return slow 
    
    def reverseList(self, head: Optional[ListNode]) -> ListNode:
        pre, cur = None, head
        while cur:
            tmp = cur.next
            cur.next = pre
            pre = cur
            cur = tmp
        return pre

    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        1 2 3 4 5
        1 1, 2 3, 3 5: stop  
        mid = 3
        list2 = 5 4 3

        1 - 5 - 2 - 4 - 3 
        exit when head2.next == None

        1 2 3 4 
        1 1, 2 3, 3 5: stop  
        mid = 3
        list2 = 4 3

        1 - 4 - 2 - 3 head2 = 4
        exit when head2.next == None

        """
        mid = self.midnode(head) #using other func in the class should be written as self.func
        head2 = self.reverseList(mid) #head2 is the head node of the second half linked list, so the list will end at midnode 
        #so the exit condition is head2.next = None 
        while head2.next:
            tmp = head.next
            tmp2 = head2.next
            head.next = head2
            head2.next = tmp
            head = tmp
            head2 = tmp2
