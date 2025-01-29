class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        left, right = 0, len(matrix) - 1
        while left < right:
            middle = left + (right - left) // 2
            if target < matrix[middle][0]:
                right = middle - 1
            else:
                # to exclude middle
                if target <= matrix[middle][-1]:
                    left = middle
                    right = middle
                else:
                    left = middle + 1

        # for thinking of the case of only 2 elements left,
        # it is not possible for target < matrix[middle][0] to happen
        row = left

        left, right = 0, len(matrix[row]) - 1
        while left < right:
            middle = left + (right - left) // 2
            if target == matrix[row][middle]: 
                return True
            elif target < matrix[row][middle]:
                right = middle - 1
            else:
                left = middle + 1

        return target == matrix[row][left]
