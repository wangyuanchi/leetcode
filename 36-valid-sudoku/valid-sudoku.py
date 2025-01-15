class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rowDict = {}
        colDict = {}
        boxDict = {} # The first key shall be (0, 0) and the last shall be (2, 2)

        for row in range(len(board)):
            for col in range(len(board)):
                current = board[row][col]
                currentBox = (row // 3, col // 3)
                
                if current == ".":
                    continue
                
                # Set up the dictionaries
                if row not in rowDict:
                    rowDict[row] = set()
                if col not in colDict:
                    colDict[col] = set()
                if currentBox not in boxDict:
                    boxDict[currentBox] = set()

                # Check if the value is already in the sets
                if current in rowDict[row] or current in colDict[col] or current in boxDict[currentBox]:
                    return False

                # Add the value into the sets
                rowDict[row].add(current)
                colDict[col].add(current)
                boxDict[currentBox].add(current)

        return True