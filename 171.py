class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        ans, pos = 0, 0
        for letter in reversed(columnTitle):
            digit = ord(letter) - 64
            ans = ans + digit * 26 ** pos
            pos = pos + 1
        return ans
        
