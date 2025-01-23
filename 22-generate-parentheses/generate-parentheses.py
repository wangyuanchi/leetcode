class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = [] # current state of the parentheses
        result = []

        def generate(leftCount, rightCount):
            if leftCount < n:
                stack.append("(")
                generate(leftCount + 1, rightCount)
                stack.pop()
            if rightCount < leftCount:
                stack.append(")")
                generate(leftCount, rightCount + 1)
                stack.pop()
            if leftCount == rightCount == n:
                result.append("".join(stack))
                
        generate(0, 0)
        return result