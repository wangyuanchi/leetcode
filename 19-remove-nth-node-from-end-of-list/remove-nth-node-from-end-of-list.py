# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # Use a sliding window of fixed size n
        # Slide from the start to the end,
        # then the node to be removed is the start of the sliding window.
        right = head
        for i in range(n - 1):
            right = right.next
        left = head

        if not right.next:
            return left.next

        prev = None
        while right.next:
            prev = left
            right = right.next
            left = left.next
            
        prev.next = left.next

        return head