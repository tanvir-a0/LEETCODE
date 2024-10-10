class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:

        if s == "" and t == "":
            return True
        
        if s == "" and t != "":
            return True
        
        if s != "" and t == "":
            return False

        matched = 0
        i = 0
        j = 0
        while True:
            print(i,j)
            if s[i] == t[j]:
                print(f"{s[i]} and {t[j]}")
                i = i + 1
                j = j + 1
                matched = matched + 1
            else:
                j = j + 1
            
            if i >= len(s) or j >= len(t):
                break
        
        if matched == len(s):
            return True
        return False

        
