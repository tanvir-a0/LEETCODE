class Solution:
    def largestOddNumber(self, num: str) -> str:
        maxx = -1
        maxx_i = 0
        for i in range(len(num)):
            if int(num[i]) % 2 == 1:
                maxx = int(num[i])
                maxx_i = i
        print(maxx)

        if maxx == -1:
            return ""
        
        return num[:maxx_i+1]

        
