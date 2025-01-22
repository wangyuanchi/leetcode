class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token not in ["+", "-", "*", "/"]:
                stack.append(int(token))
            else:
                second = stack.pop()
                first = stack.pop()

                if token == "+":
                    stack.append(first + second)
                elif token == "-":
                    stack.append(first - second)
                elif token == "*":
                    stack.append(first * second)  
                else:
                    stack.append(int(first / second)) # truncate to zero
        return stack[0]