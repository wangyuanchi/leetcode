"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None

        # first pass: insert new nodes within old nodes
        cur = head
        while cur:
            newNode = Node(cur.val)
            newNode.next = cur.next
            cur.next, cur = newNode, cur.next

        # second pass: fill in random for new nodes
        cur = head
        while cur:
            cur.next.random = cur.random.next if cur.random != None else None
            cur = cur.next.next

        # third pass: construct resulting linked list and restore original linked list
        l1 = head
        l2 = result = head.next
        while l1:
            if not l1.next.next: # Last node
                l1.next = None
                break 
            l1.next, l2.next = l1.next.next, l2.next.next
            l1, l2 = l1.next, l2.next

        return result