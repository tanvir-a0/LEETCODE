class Solution:
    def removeTrailingZeros(self, num: str) -> str:
        res = ""

        i = len(num) - 1
        while i >= 0:
            #print(i)
            if num[i] == "0":
                i = i - 1
                continue
            else:
                break
            i = i - 1
            
        return num[:i+1]
            
        
