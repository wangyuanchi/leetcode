# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        # get the head of second half
        # if even list, slow.next is head of second half when fast ends on last
        # if odd list, slow.next is head of second half when fast ends on None
        slow, fast = head, head.next
        while fast and fast.next: # breaks on last or None
            slow = slow.next
            fast = fast.next.next

        # reverse second half
        head2 = slow.next
        slow.next = None # cut the first half away from second half
        prev = None
        while head2:
            head2.next, prev, head2 = prev, head2, head2.next

        head1, head2 = head, prev

        # construct the output using 2 pointers
        while head1 and head2:
            head1.next, head2.next, head1, head2 = head2, head1.next, head1.next, head2.next