class Solution(object):
    def isValid(self, s):
        d = {'(': ')', '[': ']', '{': '}'}
        stack = []

        for ch in s:
            if ch in d:  # if it's an opening bracket
                stack.append(ch)
            else:  # it's a closing bracket
                if not stack or d[stack.pop()] != ch:
                    return False
        
        return not stack  # True if stack is empty
