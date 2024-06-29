class Solution(object):
    def lengthOfLongestSubstring(self, s):
        #print(s)
        already_there = []
        max_len_found = 0

        #print(" adfaoi", s[0:])

        if len(s) == 0:
            return 0
        
        if len(s) == 1:
            return 1

        i = 0
        while True:
            #print(already_there)
            element = s[i]

            if element in already_there:
                if max_len_found < len(already_there):
                    max_len_found = len(already_there)
                
                already_there = []
                s.index(element)
                s = s[s.index(element) + 1 : ]
                #print("converting s to ", s)
                i = -1
            
            else: 
                already_there.append(element)
            
            
            i = i + 1
            if i == len(s):
                if max_len_found < len(already_there):
                    max_len_found = len(already_there)
                break
        

        return max_len_found






s = Solution()
while True:
    print(s.lengthOfLongestSubstring(input()))