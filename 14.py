class Solution(object):
    def longestCommonPrefix(self, strs):
        i = 0
        if strs == [""]:
            return ""

        if len(strs) == 1:
            return strs[0]
        
        result = ""
        while True:
            brk = 0
            if i >= len(strs[0]):
                break

            check = strs[0][i]
            tmp = ""
            #print("check: ", check)
            for element in strs:
                if i >= len(element):
                    brk = 1
                    break
                if element[i] == check:
                    tmp = check
                else:
                    brk = 1
                    break
            if brk == 1:
                break
            else:
                result = result + tmp
            i = i + 1
            
        
        return result
        

s = Solution()
print(s.longestCommonPrefix(strs = [""]))