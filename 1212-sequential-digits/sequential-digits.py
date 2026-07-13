class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        def count_digits(value):
            digit_count = 0
            while value:
                value = value // 10
                digit_count += 1
            return digit_count

        def get_base(digit_count):
            base = 0
            for i in range(1, digit_count + 1):
                base += i * (10**(digit_count - 1))
                digit_count -= 1
            return base

        def get_increment(digit_count):
            increment = 0
            for i in range(digit_count):
                increment += 1 * (10**i)
            return increment

        def get_next_value(current_value):
            current_digit_count = count_digits(current_value)
            if current_value % 10 == 9:
                return get_base(current_digit_count + 1)
            else:
                return get_increment(current_digit_count) + current_value

        res = []
        cur_value = get_base(count_digits(low))

        while cur_value <= high:
            if cur_value >= low:
                res.append(cur_value)
            cur_value = get_next_value(cur_value)

        return res