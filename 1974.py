class Solution:
    def minTimeToType(self, word: str) -> int:
        previous = "a"
        result = 0
        for c in word:
            gap = abs(ord(c) - ord(previous))
            result = result + min(gap, abs(26-gap))
            previous = c
        
        return result + len(word)
        
