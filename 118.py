import math

class Solution(object):
    def generate(self, numRows):
        return_li = []
        for i in range(0 , numRows):
            line_no = i
            temp_li = []
            if line_no == 0:
                return_li.append([1])
                continue 
            if line_no == 1:
                return_li.append([1,1])
                continue 

            for j in range(0, i + 1):
                temp_li.append(math.comb(i,j))

            return_li.append(temp_li)

        return return_li



        
        