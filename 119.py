import math

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        return_li = []
        for i in range(0, rowIndex+1):
            return_li.append(math.comb(rowIndex, i))

        return return_li
        