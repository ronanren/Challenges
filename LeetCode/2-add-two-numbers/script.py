# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        res = ListNode()
        i = 10
        num1 = l1.val
        while(l1.next):
            l1 = l1.next
            num1 += i * l1.val
            i = i * 10

        i = 10
        num2 = l2.val
        while(l2.next):
            l2 = l2.next
            num2 += i * l2.val
            i = i * 10
        
        resInt = num1 + num2
    
        temp = res
        res.val = str(resInt)[-1]
        for j in str(resInt)[::-1][1:]:
            temp.next = ListNode()
            temp.next.val = int(j)
            temp = temp.next
            
        return res