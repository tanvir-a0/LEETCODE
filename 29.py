class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if int(dividend / divisor) < -2**31:
            return -2**31
        
        if int(dividend / divisor) > 2**31 - 1:
            return 2**31 - 1
        
        return int(dividend / divisor) 
        
