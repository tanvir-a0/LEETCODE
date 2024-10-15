class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        temp_li = []
        nc = columnNumber
        while True:
            if nc%26 == 0:
                temp_li.append(26)
                nc = nc // 26
                nc = nc - 1
            else:
                temp_li.append(nc%26)
                nc = nc // 26
            if nc <= 0:
                break
        temp_li.reverse()
        ans = ""
        for x in temp_li:
            ans = ans + chr(65+x-1)
        print(ans)
        return ans

        
