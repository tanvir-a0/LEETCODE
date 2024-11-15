class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s

        emlist =["" for i in range(numRows)]

        d = 1
        x = 0
        i = 0
        while i < len(s):
            emlist[x] = emlist[x] + s[i]

            if d == 1:
                x = x + 1
            if d == -1:
                x = x - 1
            if x == numRows - 1:
                d = -1
            if x == 0:
                d = 1

            i = i + 1

        
        res = ""
        for m in emlist:
            res = res + m
        
        return res

        
