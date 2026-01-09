# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        dummy = cur = ListNode()
        
        while l1 or l2 or carry:
            l1_val = 0 if not l1 else l1.val
            l2_val = 0 if not l2 else l2.val

            sum = l1_val + l2_val + carry
            carry = sum // 10
            res = sum % 10
            cur.next = ListNode(res)

            if l1: l1 = l1.next
            if l2: l2 = l2.next
            cur = cur.next

        return dummy.next