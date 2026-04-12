import random

class RandomizedSet:

    def __init__(self):
        self.values_dict = {}
        self.values_list = []


    def insert(self, val: int) -> bool:
        if val in self.values_dict:
            return False

        self.values_list.append(val)
        self.values_dict[val] = len(self.values_list) - 1
        return True


    def remove(self, val: int) -> bool:
        if val not in self.values_dict:
            return False
        
        val_index = self.values_dict[val]
        del self.values_dict[val]

        swapped_val = self.values_list.pop()
        if swapped_val == val:
            return True

        self.values_list[val_index] = swapped_val
        self.values_dict[swapped_val] = val_index
        return True


    def getRandom(self) -> int:
        random_index = random.randint(0, len(self.values_list) - 1)
        return self.values_list[random_index]
        

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
