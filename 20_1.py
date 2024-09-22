class Solution:
    def isValid(self, s: str) -> bool:
        count = 0
        tmp = {
            "(": ")",
            "{": "}",
            "[": "]"
        }
        stack = ""
        if len(s) % 2 == 1:
            return False
        if len(s) == 0:
            return True
        for c in s:
            if c in tmp.keys():
                stack = stack + tmp[c]
            else:
                if len(stack) == 0:
                    return False
                if c == stack[-1]:
                    stack = stack[:len(stack)-1]
                else:
                    print("returning from here middle ")
                    return False

        if len(stack) == 0:
            return True
        else:
            return False
