class Solution:
    def repeatedCharacter(self, s: str) -> str:
        for i in range(len(s)-1):
            if s[i] == s[i+1]:
                return s[i]
                
