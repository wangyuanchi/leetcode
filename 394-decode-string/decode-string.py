class Solution:
    def decodeString(self, s: str) -> str:
        def is_numeric(val: str) -> bool:
            return val in [
                "0", "1", "2",
                "3", "4", "5",
                "6", "7", "8", "9"
            ]
    
        stack = []

        for c in s:
            if c != "]":
                stack.append(c)
                continue
            
            sub_string_list = []
            while stack and stack[-1] != "[":
                sub_string_list.append(stack.pop())
            sub_string = "".join(sub_string_list[::-1])
            
            stack.pop() # pop [

            number_string = []
            while stack and is_numeric(stack[-1]):
                number_string.append(stack.pop())
            number = int("".join(number_string[::-1]))

            stack.append(sub_string * number)

        return "".join(stack)
