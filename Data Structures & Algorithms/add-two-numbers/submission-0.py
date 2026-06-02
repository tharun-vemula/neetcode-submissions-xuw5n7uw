# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        i = 0
        num1 = 0
        while l1:
            num1 += (10**i) * l1.val
            i += 1
            l1 = l1.next
        
        num2 = 0
        i = 0
        while l2:
            num2 += (10**i) * l2.val
            i += 1
            l2 = l2.next

        ans = num1 + num2
        if ans == 0:
            return ListNode(0)
        dummy = head = ListNode()
        while ans > 0:
            val = ans % 10
            ans = ans // 10
            head.next = ListNode(val)
            head = head.next
        
        return dummy.next

        
        


        