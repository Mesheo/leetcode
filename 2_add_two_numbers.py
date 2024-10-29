from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


 
class Solution: 
    def addTwoNumbers( self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        result_head = ListNode(0) 
        curr = result_head
        carry = 0 

        while l1 or l2 or carry:  
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0

            # new digit 
            sum = v1 + v2 + carry    
            new_digit = sum 
            new_digit =  sum % 10   
            carry = sum // 10 
            
            curr.next  = ListNode(new_digit) 
             
            # updating pointers 
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            curr = curr.next

        return result_head.next 