class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        max_fruits = 0
        cur_fruits = 0
        freq = {}
        l = 0
        for r in range(len(fruits)):
            if fruits[r] not in freq:
                freq[fruits[r]] = 0
            freq[fruits[r]] += 1
            cur_fruits += 1

            while len(freq) > 2:
                freq[fruits[l]] -= 1
                cur_fruits -= 1
                if freq[fruits[l]] == 0:
                    del freq[fruits[l]]
                l += 1

            max_fruits = max(max_fruits, cur_fruits)

        return max_fruits