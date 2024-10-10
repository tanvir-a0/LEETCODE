import math
class Solution(object):
    def plusOne(self, digits):
        if len(digits) == 0:
            return []
        str_digits = ""
        for c in digits:
            str_digits = str_digits + str(c)

        result_li = []
        for c in str(int(str_digits)+1):
            result_li.append(int(c))

        print(result_li)
        return result_li
        


