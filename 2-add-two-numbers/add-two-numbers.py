# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        cur1, cur2 = l1, l2
        dummy = result = ListNode()
        carryOver = 0 # either 0 or 1
        while cur1 and cur2:
            curSum = cur1.val + cur2.val + carryOver
            remainder = curSum % 10
            carryOver = int((curSum - remainder) / 10)
            dummy.next = ListNode(remainder)
            dummy, cur1, cur2 = dummy.next, cur1.next, cur2.next

        # remaining nodes from l1 or l2
        while cur1:
            curSum = cur1.val + carryOver
            remainder = curSum % 10
            carryOver = int((curSum - remainder) / 10)
            dummy.next = ListNode(remainder)
            dummy, cur1 = dummy.next, cur1.next

        while cur2:
            curSum = cur2.val + carryOver
            remainder = curSum % 10
            carryOver = int((curSum - remainder) / 10)
            dummy.next = ListNode(remainder)
            dummy, cur2 = dummy.next, cur2.next

        # deal with last carryOver
        if carryOver == 1:
            dummy.next = ListNode(carryOver)

        return result.next