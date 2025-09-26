class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return "0"

        # Make num1 the longer one so it is easier to reason about
        if len(num1) < len(num2):
            num1, num2 = num2, num1
        
        # Max number of digits in the result
        result = [0 for _ in range(len(num1) * 2 + 1)]

        for j in range(len(num2) - 1, -1, -1):
            for i in range(len(num1) - 1, -1, -1):
                # Initialize relevant indexes and values
                digit_1, digit_2 = int(num1[i]), int(num2[j])
                digit_1_index, digit_2_index = len(num1) - 1 - i, len(num2) - 1 - j
                res_index = digit_1_index + digit_2_index

                # Calculation
                res = digit_1 * digit_2 % 10
                c = (digit_1 * digit_2 - res) // 10

                # Adding to result the res and carry
                result[res_index] += res
                result[res_index + 1] += c

        # Roll forward the overflows, i.e. Addition portion
        for i in range(len(result)):
            overflowed_val = result[i]
            result[i] = overflowed_val % 10
            cur_carry = (overflowed_val - result[i]) // 10
            if i != len(result) - 1:
                result[i + 1] += cur_carry

        # Final processing
        i = len(result) - 1
        while result[i] == 0:
            i -= 1

        result = result[:i + 1]
        result.reverse()

        return "".join([str(num) for num in result])