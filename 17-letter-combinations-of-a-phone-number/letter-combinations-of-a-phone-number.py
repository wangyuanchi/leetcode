class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits == "":
            return []
            
        digitToLetter = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"],
        }

        res = []
        stringBuilder = []

        def dfs(i):
            # Base case
            if i == len(digits):
                res.append("".join(stringBuilder.copy()))
                return
            
            for c in digitToLetter[digits[i]]:
                stringBuilder.append(c)
                dfs(i + 1)
                stringBuilder.pop()

        dfs(0) 
        return res