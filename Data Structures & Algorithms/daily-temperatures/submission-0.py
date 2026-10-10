class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        zeros = [0] * len(temperatures)
        new_stack = []
        for i, temp in enumerate(temperatures):
            while new_stack and new_stack[-1][1] < temp:
                found = new_stack.pop()
                the_i = found[0]
                diff = i - the_i
                zeros[the_i] = diff
            new_stack.append((i, temp))
        return zeros
