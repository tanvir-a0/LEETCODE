def count(s, c) :
     
    # Count variable
    res = 0
     
    for i in range(len(s)) :
         
        # Checking character in string
        if (s[i] == c):
            res = res + 1
    return res

class Solution:
    def maxScore(self, s: str) -> int:
        maxx = 0

        for i in range(1,len(s)):
            #print(s[:i], s[i:])
            maxx = max(maxx, count(s[:i], "0") + count(s[i:], "1"))
        
        return maxx
        
