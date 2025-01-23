class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0]*len(temperatures)
        stack = [] # monotonic decreasing stack, (index, temp)

        for i in range(len(temperatures)):
            if len(stack) == 0 or temperatures[i] <= stack[-1][1]:
                stack.append((i, temperatures[i]))
                continue
            else:
                # temperature[i] is a "warmer" temperature
                while len(stack) > 0 and temperatures[i] > stack[-1][1]:
                    colderIndex = stack.pop()[0] # this requires a check for stack length
                    result[colderIndex] = i - colderIndex
                
                # add the "warmer" temperature to stack
                stack.append((i, temperatures[i]))

        # if there are remaining values in the stack, it's value in result is 0
        return result