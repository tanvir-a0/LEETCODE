import time

class Solution(object):
    def strStr(self, haystack, needle):
        mathched = 0
        i = 0
        j = 0
        i_breaking_point = 0
        matching_status = 0
        while True:
            #time.sleep(2)
            #print("i: ", i , " j: ", j)
            if j >= len(needle):
                return i_breaking_point
            if i >= len(haystack):
                return -1
            
            
            
            if haystack[i] == needle[j]:
                if matching_status == 0:
                    i_breaking_point = i
                    matching_status = 1

                i = i + 1
                j = j + 1
                continue
            else:
                if matching_status == 1:
                    matching_status = 0
                    i = i_breaking_point + 1
                    j = 0
                    continue
                else:
                    i = i + 1
         

s = Solution()
print(s.strStr(haystack = "asdsadbutsad", needle = "sad"))
print(s.strStr(haystack = "sadbutsad", needle = "sad"))
print(s.strStr(haystack = "aaaaa", needle = "a"))


