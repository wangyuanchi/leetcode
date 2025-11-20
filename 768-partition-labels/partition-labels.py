class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        freq = {}
        for char in s:
            if char in freq:
                freq[char] += 1
            else:
                freq[char] = 1

        res = []
        left = 0 # For calculating the total length
        window = set() # The chars in the current window
        completed = 0 # The characters that is used up completely

        for right, char in enumerate(s):
            window.add(char)
            freq[char] -= 1
            if freq[char] == 0:
                completed += 1
            if completed == len(window):
                res.append(right - left + 1)
                left = right + 1
                window = set()
                completed = 0

        return res