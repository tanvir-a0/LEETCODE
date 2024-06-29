class Solution(object):
    def isPalindrome(self, x):
        str_x = str(x)
        n = len(str_x)

        #print(str_x)

        for i in range(n):
            if str_x[i] == str_x[n - i -1 ]:
                continue
            else:
                return False
        
        return True
    

s = Solution()
print(s.isPalindrome(-40))