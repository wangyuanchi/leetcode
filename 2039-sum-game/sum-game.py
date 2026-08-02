class Solution:
    def sumGame(self, num: str) -> bool:
        sum_left = 0
        sum_right = 0
        q_left = 0
        q_right = 0
        for i, char in enumerate(num):
            if i >= len(num) / 2:
                if char == "?":
                    q_right += 1
                else:
                    sum_right += int(char)
            else:
                if char == "?":
                    q_left += 1
                else:
                    sum_left += int(char)

        # positive means right has more
        q_diff = q_right - q_left
        sum_diff = sum_right - sum_left
        
        if q_diff == 0:
            return sum_diff != 0

        # matching is from bob pov
        def can_match(sum_diff, q_diff):
            alice_turns = q_diff // 2 + q_diff % 2
            bob_turns = q_diff // 2

            if 9 * alice_turns > sum_diff:
                return False
            
            return 9 * bob_turns >= sum_diff
        
        if q_diff > 0:
            if sum_diff >= 0:
                return True

            # right has some ? and need to match sum_diff amount
            return not can_match(abs(sum_diff), q_diff)

        else:
            if sum_diff <= 0:
                return True

            # left has some ? and need to match sum_diff amount
            return not can_match(sum_diff, abs(q_diff))
            