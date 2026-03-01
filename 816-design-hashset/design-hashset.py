class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

class MyHashSet:
    def __init__(self):
        self.slots = [None] * 1000

    def get_slot(self, key: int) -> int:
        return key % 1000

    def add(self, key: int) -> None:
        if self.contains(key):
            return
            
        slot = self.get_slot(key)
        node = Node(val=key, next=self.slots[slot])
        self.slots[slot] = node

    def remove(self, key: int) -> None:
        slot = self.get_slot(key)
        cur_node = self.slots[slot]

        if not cur_node:
            return

        if cur_node.val == key:
            self.slots[slot] = cur_node.next
            return

        prev_node = None
        while cur_node:
            if cur_node.val == key:
                prev_node.next = cur_node.next
                break
            prev_node, cur_node = cur_node, cur_node.next

    def contains(self, key: int) -> bool:
        slot = self.get_slot(key)
        cur_node = self.slots[slot]
        while cur_node:
            if cur_node.val == key:
                return True
            cur_node = cur_node.next
        return False        

# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)