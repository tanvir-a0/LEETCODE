class Solution(object):
    def scoreOfString(self, s):
        
        result = 0
        if len(s) == 0:
            return 0
        if len(s) == 1:
            return int(s)
        
        for i in range(len(s)-1):
            #print("Ascii value: ", ord(s[i]), ord(s[i+1]))
            result = result + abs( ord(s[i]) - ord(s[i+1]))
        
        return result 
        
s = Solution()
print(s.scoreOfString("zaz"))