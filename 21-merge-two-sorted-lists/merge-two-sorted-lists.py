# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        cur = dummy

        while (list1 and list2):
            if list1.val <= list2.val:
                list1, cur.next = list1.next, list1
            else: 
                list2, cur.next = list2.next, list2
            cur = cur.next
        
        if list1:
            cur.next = list1
        else:
            cur.next = list2

        return dummy.next