class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        wihtout_dash = ""
        for c in s:
            if c.isalpha():
                wihtout_dash = wihtout_dash + c
                pass
            else:
                pass
        wihtout_dash = wihtout_dash[::-1]
        print(wihtout_dash)

        ans_str = ""
        i = 0
        for c in s:
            if c.isalpha() == False:
                ans_str = ans_str + c
            else:
                ans_str = ans_str + wihtout_dash[i]
                i = i + 1
        print(ans_str)

        return ans_str

        
