# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # Find the length of the linked list
        length = 1
        cur = head
        while cur.next:
            cur = cur.next
            length += 1

        slide_count = length // k
        prev, cur = None, head

        # The node that originally points to None after reversing but needs to point to some actual node
        # The index represents the window this is in
        missing_next = (0, head)

        res = None

        # Slide the window slide_count times
        for i in range(slide_count):
            temp_head = cur

            # Reverse linked list of size k, last node points to None
            for j in range(k):
                temp = cur.next
                cur.next = prev
                prev = cur
                cur = temp

            # Keep a pointer to the head for the result
            if i == 0:
                res = prev

            # Update the missing next pointer from the previous window
            if missing_next[0] + 1 == i:
                missing_next[1].next = prev
                missing_next = (i, temp_head)

            prev = None

        # Update the last missing_next
        if cur:
            missing_next[1].next = cur

        return res
