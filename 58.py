class Solution(object):
    def lengthOfLastWord(self, s):
        s = s.strip()
        #print(s)
        if len(s) == 1:
            return 1
            
        last_space = 0
        last_space_found = 0
        for i in range(len(s)-1,-1,-1):
            #print("i: ", i , s[i])
            if s[i] == " ":
                last_space = i
                last_space_found = 1
                break
        if last_space_found == 0:
            return len(s)
        
        return len(s[last_space + 1: len(s)])


        
s = Solution()
print(s.lengthOfLastWord(s = "Hello World"))
print(s.lengthOfLastWord(s = "   fly me   to   the moon  "))
print(s.lengthOfLastWord(s = "a"))
print(s.lengthOfLastWord(s = "   aaaaaaaaaaaa"))
