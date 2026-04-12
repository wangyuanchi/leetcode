import random

class RandomizedCollection:

    def __init__(self):
        self.values_dict = {} # Key: val, Value: set of indexes
        self.values_list = []   

    def insert(self, val: int) -> bool:
        new_value = False

        if val not in self.values_dict or not self.values_dict[val]:
            self.values_dict[val] = set()
            new_value = True
        
        self.values_list.append(val)
        self.values_dict[val].add(len(self.values_list) - 1)

        return new_value

    def remove(self, val: int) -> bool:
        if val not in self.values_dict or not self.values_dict[val]:
            return False

        removed_index = self.values_dict[val].pop()

        if removed_index == len(self.values_list) - 1:
            self.values_list.pop()
            return True

        popped_value = self.values_list.pop()
        self.values_list[removed_index] = popped_value
        self.values_dict[popped_value].add(removed_index)
        self.values_dict[popped_value].remove(len(self.values_list))

        return True

    def getRandom(self) -> int:
        return self.values_list[
            random.randint(0, len(self.values_list) - 1)
        ]


# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()