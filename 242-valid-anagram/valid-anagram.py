class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        letterDict = {}
        for i in s:
            if i not in letterDict:
                letterDict[i] = 1
            else:
                letterDict[i] += 1
        for i in t:
            if i not in letterDict:
                return False
            else:
                letterDict[i] -= 1
        for v in letterDict.values():
            if v != 0:
                return False
        return True