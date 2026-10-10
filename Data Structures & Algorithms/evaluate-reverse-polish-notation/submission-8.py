class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        ints = []
        operations = ['+', '-', '*', '/']
        stack = []
        for i in tokens:
            if i not in operations:
                ints.append(int(i))
            else:
                second = int(ints.pop())
                first = int(ints.pop())
                if i == '+':
                    first += second
                if i == '*':
                    first *= second
                if i == '-':
                    first -= second
                if i == '/':
                    first = int(first / second)
                ints.append(first)
        return ints.pop()