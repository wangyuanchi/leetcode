# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        
        if len(lists) == 1:
            return lists[0]

        p1, p2 = 0, 1

        while p2 <= len(lists) - 1:
            lists.append(self.merge(lists[p1], lists[p2]))
            p1 += 2
            p2 += 2

        return lists[-1]

    def merge(self, first_head, second_head):
        res = cur = ListNode()
        while first_head and second_head:
            if first_head.val < second_head.val:
                cur.next = first_head
                first_head = first_head.next
            else:
                cur.next = second_head
                second_head = second_head.next
            cur = cur.next

        if first_head:
            cur.next = first_head

        if second_head:
            cur.next = second_head

        return res.next