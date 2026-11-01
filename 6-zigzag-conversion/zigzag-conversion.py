class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        
        matrix = [[] for _ in range(numRows)]
        direction = True # True means down, False means up
        cur_row = 0
        
        for char in s:
            matrix[cur_row].append(char)
            if direction:
                cur_row += 1
                if cur_row == numRows:
                    direction = not direction
                    cur_row -= 2
            else:
                cur_row -= 1
                if cur_row == -1:
                    direction = not direction
                    cur_row += 2
                    
        res = ""
                    
        for row in matrix:
            for char in row:
                res += char
            
        return res
            
            
        
            
            