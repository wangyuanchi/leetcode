class Solution:
    def canChange(self, start: str, target: str) -> bool:
        filtered_target = []
        filtered_start = []

        for i, char in enumerate(target):
            if char != "_":
                filtered_target.append((i, char))

        for i, char in enumerate(start):
            if char != "_":
                filtered_start.append((i, char))

        if len(filtered_start) != len(filtered_target):
            return False

        for i in range(len(filtered_target)):
            if filtered_target[i][1] != filtered_start[i][1]:
                return False
                
            char = filtered_target[i][1]
            start_pos = filtered_start[i][0]
            target_pos = filtered_target[i][0]

            if char == "L" and start_pos < target_pos:
                return False

            if char == "R" and start_pos > target_pos:
                return False

        return True
