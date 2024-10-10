class Solution:
    def firstUniqChar(self, s: str) -> int:
        i = 0
        already_checked = []
        for c in s:
            # print(c, s[i+1:])
            if c not in s[i+1:] and c not in already_checked:
                return i
            already_checked.append(c)
            i = i + 1
        
        return -1
        