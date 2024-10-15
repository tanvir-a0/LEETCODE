class Solution:
    def minimumSteps(self, s: str) -> int:
        res = 0
        left = 0
        for i in range(len(s)):
            if s[i] == '0':
                res = res + (i - left)
                left = left + 1
        return res
        
