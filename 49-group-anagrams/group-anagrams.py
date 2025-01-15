class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagramDict = {} # key will be the 26 element tuple, value will be a list 
        for str in strs:
            count = [0] * 26
            for c in str:
                count[ord(c) - ord('a')] += 1 # 'a' starts at 0
            key = tuple(count)
            if key in anagramDict:
                anagramDict[key].append(str)
            else:
                anagramDict[key] = [str]
        return list(anagramDict.values())