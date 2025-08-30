class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        s = s.upper()
        newS = ""
        newNewS = ""

        for char in s:
            if char != "-":
                newS += char 
        
        # [l, r] represents the window where all char will be in the part
        l, r = len(newS) - k, len(newS) - 1

        while l >= 0:
            newNewS = newS[l:r+1] + "-" + newNewS # Additional "-"
            l -= k
            r -= k

        # Add the remaining portion from the front
        newNewS = newS[0:r+1] + "-" + newNewS

        if newNewS[0] == "-":
            newNewS = newNewS [1:]
        
        return newNewS[:-1]