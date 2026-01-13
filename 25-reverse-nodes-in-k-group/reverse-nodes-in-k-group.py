# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # Calculate the length of the linked list
        total_length = 0
        cur = head
        while cur:
            cur = cur.next
            total_length += 1
        reverse_count = total_length // k

        # Early return to prevent Null pointer
        if reverse_count == 0:
            return head

        # Perform reverse_count reversals and reverse_count - 1 linking
        cur = head
        res, link = None, None
        for i in range(reverse_count):
            original_head, reversed_head, untouched_head = self.reverseSingleGroup(cur, k)
            cur = untouched_head

            # No linking for the first reversal
            if i == 0:
                res = reversed_head
            else:
                link.next = reversed_head
            
            link = original_head

        link.next = cur

        return res
       
    def reverseSingleGroup(self, head: ListNode, k: int):
        cur = head
        prev = None
        for _ in range(k):
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp
        return head, prev, cur