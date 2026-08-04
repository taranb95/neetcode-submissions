class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        if len(s) <= 1:
            return False
        for item in s:
            print(stack)
            if not stack:
                stack.append(item)
                continue

            if item == ')':
                if stack[-1] == '(':
                    stack.pop()
                    continue
                else:
                    return False
            elif item == '}':
                if stack[-1] == '{':
                    stack.pop()
                    continue
                else:
                    return False
            elif item == ']':
                if stack[-1] == '[':
                    stack.pop()
                    continue
                else:
                    return False
            stack.append(item)
        
        if not stack:
            return True
        else:
            return False
