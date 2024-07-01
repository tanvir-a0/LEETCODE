import math
class Solution(object):
    def plusOne(self, digits):
        if len(digits) == 0:
            return []
        if len(digits) == 1:
            return digits
        main_digit = 0
        for i in range(len(digits)):
            main_digit = main_digit + int(digits[i]) * 10 ** (len(digits) - 1 - i)
        
        main_digit = main_digit + 1
        result_li = []
        while True:
            temp = main_digit % 10
            main_digit = int(main_digit/10)
            #print("temp: ", temp)
            result_li.insert(0,temp)
            
            if main_digit == 0:
                break
            
    
        return result_li
        

s = Solution()
print(s.plusOne(digits = []))
