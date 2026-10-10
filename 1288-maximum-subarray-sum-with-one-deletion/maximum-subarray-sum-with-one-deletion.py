class Solution:
    def maximumSum(self, arr: list[int]) -> int:
        max_no_delete = max_one_delete = result = arr[0]

        for i in range(1, len(arr)):
            max_one_delete = max(max_one_delete + arr[i], max_no_delete)
            max_no_delete = max(max_no_delete + arr[i], arr[i])
            result = max(result, max_no_delete, max_one_delete)
            
        return result