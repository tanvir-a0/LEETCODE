class Solution:
    def is_palindrome(self, s):
        for i in range(int(len(s)/2)):
            if s[i] == s[int(len(s)) - 1 - i]:
                continue
            else:
                return False
        return True
        
    def longestPalindrome(self, s: str) -> str:
        anss = ""
        maxx = 0
        for i in range(len(s)):
            for j in range(len(s)):
                if (i > j): 
                    j = j + 1
                else:
                    subs = s[i:j+1]
                    print(subs)

                    if self.is_palindrome(subs) and (len(subs) > maxx):
                        maxx = len(subs)
                        anss = subs
        
        return anss
