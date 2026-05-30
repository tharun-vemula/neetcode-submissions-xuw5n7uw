class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for char in s:
            if char == "(" or char == "{" or char == "[":
                stack.append(char)
            else:
                if not stack:
                    return False
                last = stack.pop()
                if last == "(" and char != ")":
                    return False
                if last == "{" and char != "}":
                    return False
                if last == "[" and char != "]":
                    return False
        return len(stack) == 0
        