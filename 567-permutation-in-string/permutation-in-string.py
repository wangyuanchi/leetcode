class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        alphabet = [0] * 26

        for c in s1:
            alphabet[ord(c) - ord('a')] += 1
        for c in s2[0:len(s1)]:
            alphabet[ord(c) - ord('a')] -= 1

        totalMismatch = 0
        for num in alphabet:
            if num != 0:
                totalMismatch += 1
        
        # check for first window
        if totalMismatch == 0:
            return True

        left = 0
        for right in range(len(s1), len(s2)):
            leftAlphabetIndex = ord(s2[left]) - ord('a')
            alphabet[leftAlphabetIndex] += 1
            if alphabet[leftAlphabetIndex] == 0:
                totalMismatch -= 1
            elif alphabet[leftAlphabetIndex] == 1:
                totalMismatch += 1
            # else do nothing and continue

            left += 1

            rightAlphabetIndex = ord(s2[right]) - ord('a')
            alphabet[rightAlphabetIndex] -= 1
            if alphabet[rightAlphabetIndex] == 0:
                totalMismatch -= 1
            elif alphabet[rightAlphabetIndex] == -1:
                totalMismatch += 1
            # else do nothing and continue

            # check for all other windows
            if totalMismatch == 0:
                return True

        return False