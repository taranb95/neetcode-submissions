class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        token = ['+', '-', '*', '/']
        res = 0
        for num in tokens:
            print(res)
            if num not in token:
                stack.append(num)
            else:
                # if res == 0:
                    num1 = stack.pop()
                    num2 = stack.pop()
                    if num == '+':
                        res = int(num1) + int(num2)
                    elif num == '-':
                        res = int(num2) - int(num1)
                    elif num == '*':
                        res = int(num1) * int(num2)
                    else:
                        res = int(num2) / int(num1)
                    stack.append(res)
                # else:
                #     if num == '+':
                #         res = res + int(stack.pop())
                #     elif num == '-':
                #         res = res - int(stack.pop())
                #     elif num == '*':
                #         res = res * int(stack.pop())
                #     else:
                #         res = res / int(stack.pop())
        return int(stack.pop())
        